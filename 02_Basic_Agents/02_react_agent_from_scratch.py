import os
import re
from dotenv import load_dotenv
from openai import OpenAI

# .env dosyasından API anahtarını yükle
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    # Eğer .env yoksa veya key yoksa, burada hata fırlatabiliriz veya kullanıcıdan isteyebiliriz.
    # Şimdilik uyarı verip devam edelim (API calls fail edecektir).
    print("UYARI: OPENAI_API_KEY bulunamadı. Lütfen .env dosyasını kontrol edin.")

client = OpenAI(api_key=api_key)

# --- TOOLS ---
def search_wikipedia(query):
    """
    Basit bir 'arama' simülasyonu. 
    Gerçek bir uygulamada burada Wikipedia API veya Google Search API kullanılır.
    """
    print(f"\n[TOOL] Wikipedia'da aranıyor: {query}")
    # Mock data
    valid_data = {
        "Atatürk": "Mustafa Kemal Atatürk (1881-1938), Türk mareşal ve devlet adamı, Türkiye Cumhuriyeti'nin kurucusu.",
        "Python": "Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir.",
        "Yapay Zeka": "Yapay zeka (YZ), insan zekasını taklit eden makineler geliştirmeyi amaçlayan bir bilgisayar bilimi dalıdır."
    }
    
    # Basit bir "contains" check
    for key, value in valid_data.items():
        if key.lower() in query.lower():
            return value
    
    return "Aranan terim hakkında bilgi bulunamadı. (Mock data sınırlı)"

def calculate(expression):
    """
    Basit matematiksel hesaplama aracı.
    """
    print(f"\n[TOOL] Hesaplanıyor: {expression}")
    try:
        # Güvenlik riski: eval() kullanımı prodüksiyonda tehlikelidir, demo için kullanıyoruz.
        # Sadece sayı ve işlem işaretlerine izin verilmeli.
        allowed = set("0123456789+-*/(). ")
        if not set(expression).issubset(allowed):
            return "Hata: Geçersiz karakterler."
        return str(eval(expression))
    except Exception as e:
        return f"Hesaplama hatası: {e}"

# Tool listesi ve tanımları
tools = {
    "search": search_wikipedia,
    "calculate": calculate
}

TOOL_DESCRIPTIONS = """
1. search: Bir konu hakkında bilgi almak için kullanılır. Girdi bir arama terimidir.
2. calculate: Matematiksel hesaplama yapmak için kullanılır. Girdi bir matematiksel ifadedir (örn: 2+2).
"""

# --- SYSTEM PROMPT (ReAct Pattern) ---
REACT_SYSTEM_PROMPT = """
Sen, 'Reasoning' ve 'Acting' (ReAct) döngüsünü kullanan zeki bir asistansın.
Bir soruya cevap vermek için şu formatı KESİNLİKLE takip etmelisin:

Soru: Kullanıcının sorduğu soru.
Düşünce: Yapman gereken adımı düşün. (Hangi aracı kullanmalıyım? Neyi bulmalıyım?)
Aksiyon: [tool_name]
Aksiyon Girdisi: [tool_input]
Gözlem: Aracın çıktısı (Bu sana sistem tarafından verilecek).
... (Bu Düşünce/Aksiyon/Gözlem döngüsü cevabı bulana kadar tekrar edebilir)
Düşünce: Artık son cevabı biliyorum.
Son Cevap: Kullanıcıya verilecek nihai yanıt.

Mevcut Araçlar:
{tool_descriptions}

Örnek:
Soru: Atatürk kaç yılında doğdu ve bu sayı 2 ile çarpılınca kaç eder?
Düşünce: Önce Atatürk'ün doğum yılını bulmalıyım. search aracını kullanabilirim.
Aksiyon: search
Aksiyon Girdisi: Atatürk
Gözlem: Mustafa Kemal Atatürk (1881-1938)...
Düşünce: Doğum yılı 1881. Şimdi bunu 2 ile çarpmalıyım.
Aksiyon: calculate
Aksiyon Girdisi: 1881 * 2
Gözlem: 3762
Düşünce: Son cevabı buldum.
Son Cevap: Atatürk 1881 yılında doğmuştur ve bu sayının 2 katı 3762 eder.

Şimdi başla!
"""

def react_loop(user_query, max_steps=5):
    messages = [
        {"role": "system", "content": REACT_SYSTEM_PROMPT.format(tool_descriptions=TOOL_DESCRIPTIONS)},
        {"role": "user", "content": f"Soru: {user_query}"}
    ]
    
    print(f"DEBUG: Starting ReAct loop for query: '{user_query}'")
    
    for i in range(max_steps):
        # 1. LLM'den yanıt al
        response = client.chat.completions.create(
            model="gpt-4o",  # gpt-3.5-turbo veya gpt-4
            messages=messages,
            stop=["Gözlem:"] # LLM'in kendisi Gözlem uydurmasın diye durduruyoruz.
        )
        
        llm_output = response.choices[0].message.content
        print(f"\n--- Adım {i+1} ---")
        print(llm_output)
        
        # Mesaj geçmişine ekle
        messages.append({"role": "assistant", "content": llm_output})
        
        # 2. "Son Cevap" var mı kontrol et
        if "Son Cevap:" in llm_output:
            return llm_output.split("Son Cevap:")[1].strip()
        
        # 3. Aksiyonu parse et
        # Regex ile Aksiyon ve Aksiyon Girdisi'ni yakala
        # Format:
        # Aksiyon: search
        # Aksiyon Girdisi: Atatürk
        
        action_match = re.search(r"Aksiyon:\s*(\w+)", llm_output)
        input_match = re.search(r"Aksiyon Girdisi:\s*(.*)", llm_output)
        
        if action_match and input_match:
            tool_name = action_match.group(1).strip()
            tool_input = input_match.group(1).strip()
            
            # 4. Aracı çalıştır
            if tool_name in tools:
                observation = tools[tool_name](tool_input)
            else:
                observation = f"Hata: '{tool_name}' diye bir araç yok."
                
            print(f"Gözlem: {observation}")
            
            # 5. Gözlemi LLM'e geri besle
            messages.append({"role": "user", "content": f"Gözlem: {observation}"})
        else:
            # LLM formatı bozduysa veya sadece düşünüyorsa
            # Genelde bir sonraki adımda toparlaması için uyarı verebiliriz veya devam ederiz.
            if "Düşünce:" in llm_output and not "Aksiyon:" in llm_output:
                # Sadece düşünüyor olabilir, devam etsin ama sonsuz döngüye girmesin diye bir şey yapmıyoruz.
                pass
            else:
                print("Format hatası veya aksiyon bulunamadı.")
                # break # veya continue

    return "Maksimum adım sayısına ulaşıldı, cevap bulunamadı."

if __name__ == "__main__":
    print("🏁 ReAct Ajan Demo (Manuel Implementasyon)")
    print("Örnek soru: 'Atatürk kaç yılında doğdu ve 2024 ile arasındaki fark nedir?'")
    print("-" * 60)
    
    while True:
        try:
            q = input("\nSoru (Çıkış için 'q'): ")
            if q.lower() == 'q':
                break
            
            final_answer = react_loop(q)
            print(f"\n✅ NİHAİ CEVAP: {final_answer}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Hata: {e}")
