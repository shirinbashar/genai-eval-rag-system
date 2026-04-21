def load_documents():
    with open("data/sample.txt", "r") as f:
        text = f.read()
    return text


def chunk_text(text, chunk_size=100):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))

    return chunks


def retrieve_relevant_chunk(query, chunks):
    query_words = query.lower().split()

    best_chunk = ""
    best_score = 0

    for chunk in chunks:
        score = sum(word in chunk.lower() for word in query_words)

        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk