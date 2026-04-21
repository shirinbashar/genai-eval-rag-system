# 🧠 GenAI Evaluation & RAG Prototype System

A Python-based Generative AI system that demonstrates **Retrieval-Augmented Generation (RAG)** combined with a **lightweight evaluation framework** for assessing LLM response quality.

This project simulates real-world GenAI workflows used in enterprise and federal environments, focusing on **grounded responses, observability, and model evaluation**.

---

# 🚀 Key Features

## 🔹 1. Retrieval-Augmented Generation (RAG)
- Loads and processes local text documents
- Splits documents into chunks for retrieval
- Retrieves relevant context using lightweight keyword matching
- Injects retrieved context into LLM prompts

## 🔹 2. LLM Integration
- Uses OpenAI Chat Completions API
- Generates context-aware responses
- Structured prompt engineering for grounded outputs

## 🔹 3. Evaluation Framework
Implements a simple but effective scoring system:

- **Relevance Score** → How well the response matches the query
- **Context Usage Score** → How much retrieved context is reflected in output
- **Hallucination Risk Score** → Estimates likelihood of unsupported claims

## 🔹 4. Observability & Logging
- Logs prompts and responses to JSON
- Stores evaluation metrics in CSV format
- Enables traceability of AI outputs

---

# 🧱 System Architecture

```text
User Query
   ↓
Document Loader (data/sample.txt)
   ↓
Text Chunking (RAG preprocessing)
   ↓
Context Retrieval (keyword-based similarity)
   ↓
Prompt Construction (context + query)
   ↓
LLM Generation (OpenAI GPT-4o-mini)
   ↓
Evaluation Layer (scoring system)
   ↓
Logging & Metrics Storage (JSON + CSV)

🛠️ Tech Stack
Python 3.10+
OpenAI API (GPT-4o-mini)
Requests
Pandas
Python-dotenv

▶️ How to Run
1. Clone the repository
git clone https://github.com/your-username/genai-eval-rag-system.git
cd genai-eval-rag-system
2. Install dependencies
pip install -r requirements.txt
3. Add environment variables
Create a .env file:
OPENAI_API_KEY=your_api_key_here
4. Run the application
python app.py

📊 Example Output
LLM Response:
AI is used in healthcare for diagnosis, predictive analytics, and patient monitoring...
Evaluation Metrics:
Relevance Score        : 0.80
Context Usage Score    : 0.70
Hallucination Risk     : 0.30
🧠 What This Project Demonstrates

This project showcases:

End-to-end GenAI application design
RAG-based architecture fundamentals
Prompt engineering with contextual grounding
AI evaluation and scoring techniques
Logging and observability for AI systems
Basic AI governance thinking (hallucination tracking)
