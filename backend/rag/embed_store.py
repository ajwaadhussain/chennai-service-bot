import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load a small, fast local model (downloaded once)
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts: list[str]) -> np.ndarray:
    # Convert text to numbers using your CPU
    vectors = model.encode(texts)
    # Normalize for better search
    faiss.normalize_L2(vectors)
    return vectors

def build_and_save_index(chunks: list[str], index_path: str, meta_path: str):
    print("🧠 Generating embeddings locally... (Free!)")
    vectors = embed_texts(chunks)
    dim = vectors.shape[1]
    
    index = faiss.IndexFlatIP(dim)
    index.add(vectors)

    faiss.write_index(index, index_path)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump({"chunks": chunks}, f, ensure_ascii=False, indent=2)
    print("✅ Index built and saved!")

def load_index(index_path: str, meta_path: str):
    index = faiss.read_index(index_path)
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    return index, meta["chunks"]