from rag import load_documents, chunk_text, retrieve_relevant_chunk
from evaluator import evaluate_response, save_evaluation
import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")


# ---------------------------
# LLM CALL FUNCTION
# ---------------------------
def query_llm(prompt):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result["choices"][0]["message"]["content"]


# ---------------------------
# LOGGING FUNCTION
# ---------------------------
def save_output(prompt, response):
    os.makedirs("outputs", exist_ok=True)

    data = {
        "timestamp": str(datetime.now()),
        "prompt": prompt,
        "response": response
    }

    with open("outputs/log.json", "a") as f:
        f.write(json.dumps(data) + "\n")


# ---------------------------
# MAIN RAG PIPELINE
# ---------------------------
if __name__ == "__main__":

    # 1. User query
    query = "how does Machine Learning analyze images?"

    # 2. Load documents
    docs = load_documents()
    chunks = chunk_text(docs)

    # 3. Retrieve relevant context (RAG step)
    context = retrieve_relevant_chunk(query, chunks)

    # 4. Build final prompt (THIS is RAG injection)
    prompt = f"""
Use the context below to answer the question.

CONTEXT:
{context}

QUESTION:
{query}
"""

    # 5. Call LLM
    answer = query_llm(prompt)

    # 6. Evaluate response (ADD THIS)
    metrics = evaluate_response(query, answer, context)

    # 7. Save logs (existing logging)
    save_output(query, answer)

    # 8. Save evaluation results (NEW)
    save_evaluation(query, answer, context, metrics)

    # 9. Print result
    print("\n--- FINAL ANSWER ---\n")
    print(answer)


    #10. Print evaluation metrics (ADD THIS HERE)
    print("\n--- EVALUATION METRICS ---")
    print(f"Relevance Score        : {metrics['relevance']}")
    print(f"Context Usage Score    : {metrics['context_usage']}")
    print(f"Hallucination Risk     : {metrics['hallucination_risk']}")