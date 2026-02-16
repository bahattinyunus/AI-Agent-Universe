# 🧠 AI Agent Concepts: From Zero to Hero

Bu döküman, yapay zeka ajanlarının temel kavramlarını, çalışma prensiplerini ve mimari farklılıklarını anlamak için hazırlanmıştır.

## 1. AI Agent Nedir?

Bir **AI Agent (Yapay Zeka Ajanı)**, çevresini algılayan, kararlar alan ve belirli bir hedefe ulaşmak için aksiyonlar gerçekleştiren otonom bir sistemdir.

Standart bir LLM (örn: ChatGPT) pasiftir; siz sorarsınız, o cevaplar. Bir Agent ise:
1.  **Düşünür (Reasoning):** "Bu sorunu çözmek için ne yapmalıyım?"
2.  **Planlar (Planning):** "Önce X'i araştırmalı, sonra Y'yi hesaplamalıyım."
3.  **Araç Kullanır (Tool Use):** "İnternette arama yapayım" veya "Python kodu çalıştırayım."
4.  **Uygular (Action):** "Sonucu kullanıcıya raporlayayım."

---

## 2. Reasoning (Akıl Yürütme) Teknikleri

Ajanların "düşünme" sürecini simüle etmek için kullanılan başlıca prompt teknikleri:

### 🔗 Chain of Thought (CoT)
Karmaşık bir problemi adım adım çözme tekniğidir.
*   **Standart:** "Ali'nin 5 elması var, 2'sini yedi, sonra 3 tane daha aldı. Kaç elması var?" -> "6"
*   **CoT:** "Ali'nin başta 5 elması vardı. 2 tanesini yedi, geriye 3 kaldı. Sonra 3 tane daha aldı, 3 + 3 = 6. Cevap 6."

### ⚛️ ReAct (Reason + Act)
Ajanın düşünme ve eyleme geçme döngüsüdür.
1.  **Thought:** Kullanıcı hava durumunu sordu.
2.  **Action:** `get_weather(city="Istanbul")` fonksiyonunu çağır.
3.  **Observation:** API'den "22°C, Güneşli" yanıtı geldi.
4.  **Final Answer:** "İstanbul'da hava şu an 22 derece ve güneşli."

---

## 3. Ajan Mimarileri

### 👤 Single-Agent (Tekil Ajan)
Tek bir LLM'in tüm süreci yönettiği yapıdır. Genellikle basit, lineer görevler için uygundur.
*   **Örnek:** Sadece PDF özetleyen bir asistan.

### 👥 Multi-Agent (Çoklu Ajan)
Farklı "kişiliklere" ve "yeteneklere" sahip birden fazla ajanın iş birliği yaptığı yapıdır.
*   **Manager Agent:** Görevleri dağıtır.
*   **Researcher Agent:** Bilgi toplar.
*   **Writer Agent:** Toplanan bilgiyi raporlar.
*   **Reviewer Agent:** Raporu kontrol eder ve düzeltme ister.

*Frameworkler:* CrewAI, Microsoft AutoGen.
