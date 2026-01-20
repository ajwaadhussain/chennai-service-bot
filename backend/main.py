import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <-- The Bridge Tool
from pydantic import BaseModel

from rag.pdf_to_text import pdf_to_text
from rag.chunking import chunk_text
from rag.embed_store import build_and_save_index, load_index
from rag.rag_answer import retrieve, generate_answer

app = FastAPI()

# --- THE BRIDGE (CORS) ---
# This allows the frontend (port 5173) to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -------------------------

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
PDF_PATH = os.path.join(DATA_DIR, "chennai_services.pdf")
INDEX_PATH = os.path.join(DATA_DIR, "index.faiss")
META_PATH = os.path.join(DATA_DIR, "chunks.json")

index = None
chunks = None

class ChatIn(BaseModel):
    message: str

@app.on_event("startup")
def startup_event():
    global index, chunks
    if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
        index, chunks = load_index(INDEX_PATH, META_PATH)
        print("✅ Loaded existing index from disk.")
    else:
        print("⚠️ No index found. Please call /ingest endpoint.")

@app.post("/ingest")
def ingest():
    global index, chunks
    text = pdf_to_text(PDF_PATH)
    new_chunks = chunk_text(text, chunk_tokens=300, overlap_tokens=50)
    build_and_save_index(new_chunks, INDEX_PATH, META_PATH)
    index, chunks = load_index(INDEX_PATH, META_PATH)
    return {"status": "success", "chunks_count": len(chunks)}

@app.post("/chat")
def chat(payload: ChatIn):
    global index, chunks
    if index is None:
        return {"answer": "I haven't learned the PDF yet! Please run the ingest step first."}
    hits = retrieve(payload.message, index, chunks)
    answer = generate_answer(payload.message, hits)
    return {"answer": answer, "sources": hits}