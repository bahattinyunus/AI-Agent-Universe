import os
from dotenv import load_dotenv
from openai import OpenAI

# .env dosyasından API anahtarını yükle
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Lütfen .env dosyanıza OPENAI_API_KEY ekleyin.")

client = OpenAI(api_key=api_key)

def simple_agent(user_query):
    """
    Basit bir 'tekil ajan' (single-agent) simülasyonu.
    Şimdilik sadece bir sistem promt'u ile LLM'e kimlik kazandırıyoruz.
    """
    
    system_prompt = """
    Sen yardımsever ve profesyonel bir yapay zeka asistanısın.
    Karmaşık konuları basit metaforlarla açıklamayı seversin.
    Her zaman Türkçe yanıt ver.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",  # veya gpt-3.5-turbo
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    print("🤖 Basit Ajan Başlatıldı (Çıkış için 'q' yazın)")
    print("-" * 50)
    
    while True:
        user_input = input("\nSiz: ")
        if user_input.lower() == 'q':
            print("Görüşmek üzere!")
            break
            
        print("Ajan düşünüyor...")
        try:
            answer = simple_agent(user_input)
            print(f"Ajan: {answer}")
        except Exception as e:
            print(f"Hata oluştu: {e}")
