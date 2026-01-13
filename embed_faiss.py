import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load Tamil chunks
with open("tamil_chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Loaded {len(chunks)} chunks")

# Load multilingual embedding model
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# Create embeddings
embeddings = model.encode(
    chunks,
    show_progress_bar=True,
    convert_to_numpy=True,
    normalize_embeddings=True
)

print("Embeddings shape:", embeddings.shape)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)  # cosine similarity
index.add(embeddings)

print("FAISS index size:", index.ntotal)

# Save FAISS index
faiss.write_index(index, "tamil_faiss.index")

# Save chunks for lookup
with open("tamil_chunks_lookup.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

print("FAISS index and lookup file saved")
