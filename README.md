

# 🤖 AI Agent Master: Learning & Implementation Hub

Bu depo (repository), LLM'lerin (Büyük Dil Modelleri) sadece metin üretmekten çıkıp, **akıl yürüten (reasoning)**, **planlama yapan (planning)** ve **araç kullanan (tool use)** otonom ajanlara dönüşüm sürecini kapsamaktadır.

Buradaki amacım, AI Agent mimarilerini öğrenmek, farklı frameworkleri (LangChain, CrewAI, AutoGen) test etmek ve gerçek dünya senaryolarına uygun ajanlar geliştirmektir.

---

## 🏗️ AI Agent Mimarisi (Nasıl Çalışır?)

Bir AI Agent, temel olarak bir LLM'in şu bileşenlerle birleşmesidir:

1. **Planning (Planlama):** Karmaşık bir görevi küçük, yönetilebilir adımlara bölme yeteneği (Chain of Thought, Tree of Thoughts).
2. **Memory (Bellek):** * *Short-term:* Bağlam içi öğrenme (In-context learning) ve sohbet geçmişi.
* *Long-term:* Vektör veritabanları (RAG) aracılığıyla sınırsız bilgiye erişim.


3. **Tool Use (Araç Kullanımı):** API'ler, hesap makineleri, Python interpreter veya arama motorları gibi dış dünyaya açılan kapılar.
4. **Action (Aksiyon):** Planlanan adımların araçlar vasıtasıyla icra edilmesi.

---

## 🛠️ Teknoloji Yığını (Stack)

Bu repoda kullanılan ve üzerinde çalışılan ana teknolojiler:

| Kategori | Teknolojiler |
| --- | --- |
| **LLM Sağlayıcılar** | OpenAI (GPT-4o), Anthropic (Claude 3.5), Google (Gemini 1.5 Pro) |
| **Local LLM** | Ollama, LM Studio (Llama 3, Mistral) |
| **Frameworkler** | LangChain, LangGraph, CrewAI, Microsoft AutoGen |
| **Veritabanları** | Pinecone, ChromaDB, Weaviate (Vektör Veritabanları) |
| **Araçlar / API** | Tavily (Search), Serper, Python REPL, SQL Database |

---

## 📂 Repository Klasör Yapısı

Projeler ve öğrenme materyalleri aşağıdaki hiyerarşide düzenlenmiştir:

* `01_Theory/`: Ajanların arkasındaki akademik makaleler ve mimari notlar (ReAct, Reflexion).
* `02_Basic_Agents/`: Tek bir amaca hizmet eden basit ajan yapıları (Single-Agent).
* `03_Multi_Agent_Systems/`: Birden fazla ajanın birbiriyle iş birliği yaptığı yapılar (CrewAI & AutoGen).
* `04_Memory_and_RAG/`: Hafıza yönetimi ve döküman tabanlı ajan uygulamaları.
* `05_Deployment/`: Ajanların API (FastAPI) veya arayüz (Streamlit/Chainlit) ile yayına alınması.

---

## 🚀 Öne Çıkan Projelerim

### 🕵️‍♂️ Otonom Pazar Araştırmacısı

İnterneti tarayarak rakip analizi yapan, verileri tablolaştıran ve nihai bir PDF raporu hazırlayan çoklu-ajan sistemi.

* **Kullanılan:** CrewAI + Tavily + GPT-4o.

### 💻 AI Software Engineer

Verilen bir prompt ile tüm bir Python projesini yazan, hataları test eden ve düzelten (Self-Correction) ajan.

* **Kullanılan:** LangGraph + Python Interpreter.

### 📞 Akıllı Müşteri Destek Ajanı

Şirket dökümanlarını (PDF/Notlar) okuyan ve müşterilere kurumsal dille cevap veren RAG destekli ajan.

* **Kullanılan:** Pinecone + LangChain + Claude 3.5.

---

## 📚 Öğrenme Yol Haritası (Roadmap)

Ajanları öğrenirken takip ettiğim (veya edeceğim) adımlar:

1. [x] **Prompt Engineering:** Few-shot, ReAct ve Chain of Thought teknikleri.
2. [x] **Function Calling:** LLM'lerin dış fonksiyonları çağırmasını sağlamak.
3. [ ] **State Management:** Uzun süreli konuşmalarda durum yönetimi (LangGraph).
4. [ ] **Evaluations:** Ajanların performansını ölçümleme (Trulens, Ragas).
5. [ ] **Deployment:** Ajanları ölçeklenebilir bir mimaride sunma.

---

## 📝 Kurulum ve Çalıştırma

Projeleri yerelinizde çalıştırmak için:

1. **Repoyu Klonlayın:**
```bash
git clone https://github.com/kullanici-adiniz/ai-agent-master.git
cd ai-agent-master

```


2. **Sanal Ortam Oluşturun:**
```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

```


3. **Bağımlılıkları Yükleyin:**
```bash
pip install -r requirements.txt

```


4. **Ortam Değişkenlerini Ayarlayın:**
`.env.example` dosyasını `.env` olarak kopyalayın ve API anahtarlarınızı girin.

---

## 🤝 Katkıda Bulunma

Yeni fikirler veya hata düzeltmeleri için Pull Request açmaktan çekinmeyin. Birlikte daha akıllı ajanlar inşa edelim!

---

*Bu depo [Tarih] tarihinde oluşturulmuştur ve sürekli güncellenmektedir.*

---

