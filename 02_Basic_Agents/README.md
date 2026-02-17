# 02_Basic_Agents

Bu klasör, tekil ajan (single-agent) yapılarının ve temel ajan tasarım desenlerinin (Design Patterns) örneklerini içerir.

## İçerik

1.  **simple_agent_template.py**:
    *   En temel LLM çağrısı örneği.
    *   Sadece bir sistem promptu (System Prompt) ile motora "rol" (persona) kazandırılır.
    *   Araç kullanımı (Tool use) veya hafıza (Memory) yoktur.

2.  **02_react_agent_from_scratch.py**:
    *   **ReAct (Reason + Act)** deseninin *manuel* implementasyonudur.
    *   Herhangi bir framework (LangChain vb.) kullanmadan, "Düşünce -> Aksiyon -> Gözlem" döngüsünün nasıl çalıştığını gösterir.
    *   **Dahili Araçlar:**
        *   `search_wikipedia`: Basit bir bilgi arama simülasyonu.
        *   `calculate`: Matematiksel işlem aracı.
    *   **Nasıl Çalışır?**
        *   LLM'e özel bir prompt verilir (bkz. `REACT_SYSTEM_PROMPT`).
        *   LLM, bir araç kullanmak istediğinde özel bir formatta yanıt döner (`Aksiyon: ...`).
        *   Python kodu bu formatı parse eder, ilgili fonksiyonu çalıştırır ve sonucu `Gözlem:` olarak tekrar LLM'e gönderir.

## Nasıl Çalıştırılır?

Öncelikle ana dizindeki `.env` dosyanızda `OPENAI_API_KEY` tanımlı olduğundan emin olun.

```bash
# Basit ajanı çalıştırmak için:
python 02_Basic_Agents/simple_agent_template.py

# ReAct ajanını çalıştırmak için:
python 02_Basic_Agents/02_react_agent_from_scratch.py
```
