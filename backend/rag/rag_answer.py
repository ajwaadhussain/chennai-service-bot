import os
import numpy as np
import faiss
import google.generativeai as genai
from sentence_transformers import SentenceTransformer

# 1. Setup Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
chat_model = genai.GenerativeModel('gemini-flash-latest')

# 2. Setup Local Embeddings (Must match embed_store.py)
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_query(query: str) -> np.ndarray:
    vec = embed_model.encode([query])
    faiss.normalize_L2(vec)
    return vec

def retrieve(query: str, index, chunks: list[str], k: int = 4) -> list[str]:
    qvec = embed_query(query)
    scores, ids = index.search(qvec, k)
    
    results = []
    for i in ids[0]:
        if i == -1: continue
        results.append(chunks[i])
    return results

def generate_answer(user_question: str, retrieved_chunks: list[str]) -> str:
    context = "\n\n".join(retrieved_chunks)
    
    prompt = (
        "You are a helpful Chennai Local Guide assistant. "
        "Use ONLY the provided Context to answer the question. "
        "If the answer is not in the context, say 'I don't have that information'.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{user_question}"
    )

    response = chat_model.generate_content(prompt)
    return response.text