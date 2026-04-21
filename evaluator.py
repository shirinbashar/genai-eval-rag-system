import pandas as pd
import os
from datetime import datetime

def evaluate_response(query, response, context):
    query_words = query.lower().split()
    response_words = response.lower().split()
    context_words = context.lower().split()

    # -----------------------
    # 1. Relevance score
    # -----------------------
    relevance = sum(word in response_words for word in query_words) / len(query_words)

    # -----------------------
    # 2. Context usage score
    # -----------------------
    context_usage = sum(word in response_words for word in context_words) / max(len(context_words), 1)

    # -----------------------
    # 3. Hallucination risk (simple heuristic)
    # If response uses few context words → higher risk
    # -----------------------
    hallucination_risk = 1 - context_usage

    return {
        "relevance": round(relevance, 2),
        "context_usage": round(context_usage, 2),
        "hallucination_risk": round(hallucination_risk, 2)
    }

def save_evaluation(query, response, context, metrics):
    os.makedirs("outputs", exist_ok=True)

    row = {
        "timestamp": str(datetime.now()),
        "query": query,
        "response": response,
        "context": context,
        "relevance": metrics["relevance"],
        "context_usage": metrics["context_usage"],
        "hallucination_risk": metrics["hallucination_risk"]
    }

    file_path = "outputs/evaluation.csv"

    df = pd.DataFrame([row])

    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode="a", header=False, index=False)