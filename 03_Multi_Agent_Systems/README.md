# 03_Multi_Agent_Systems

Bu klasör, birden fazla ajanın iş birliği yaparak (collaborative) karmaşık görevleri çözdüğü sistemleri içerir.

## Planlanan İçerik (Roadmap)

1.  **CrewAI Başlangıç:**
    *   Researcher ve Writer ajanlarının blog yazısı yazmak için iş birliği yapması.
    *   `src/crew_blog_writer.py` (Yakında)

2.  **AutoGen Sohbeti:**
    *   İki ajanın (örneğin Satıcı ve Alıcı) bir ürün fiyatı üzerine pazarlık yapması.
    *   `src/autogen_negotiation.py` (Yakında)

3.  **Hierarchical Teams:**
    *   Bir "Manager" ajanın, alt ajanlara (Worker) görev dağıtıp sonuçları topladığı hiyerarşik yapı.

## Neden Çoklu Ajan?

Tek bir LLM'in (veya ajanın) bağlam penceresi (context window) ve yetenekleri sınırlıdır. Çoklu ajan sistemleri:
*   **Uzmanlaşma:** Her ajan sadece kendi işine odaklanır (Biri kod yazar, biri test eder).
*   **Hata Kontrolü:** Bir ajan hata yaparsa, diğer ajan (Reviewer) bunu yakalayabilir.
*   **Paralelizasyon:** Farklı görevler aynı anda yürütülebilir.
