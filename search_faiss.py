import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load FAISS index
index = faiss.read_index("tamil_faiss.index")

# Load chunk lookup
with open("tamil_chunks_lookup.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Load same embedding model
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def search(query, top_k=3):
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    scores, indices = index.search(query_embedding, top_k)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        results.append({
            "score": float(score),
            "text": chunks[idx]
        })

    return results


# -------- TEST QUERY --------
query = "UPSC தேர்வு என்றால் என்ன?"
results = search(query)

print("\nQuery:", query)
print("\nTop Results:\n")

for i, r in enumerate(results, 1):
    print(f"{i}. Score: {r['score']:.3f}")
    print(r["text"])
    print("-" * 60)
