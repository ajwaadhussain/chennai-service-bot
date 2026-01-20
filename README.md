# 🤖 Chennai Services AI (RAG Prototype)

A full-stack AI chatbot that helps users find local services in Chennai (Hospitals, Transport, Utilities). It uses **Retrieval-Augmented Generation (RAG)** to "read" a local knowledge base and answer questions accurately using Google's Gemini AI.

## 🚀 Why This Project?
Traditional chatbots hallucinate (make things up). This project solves that by using **RAG**:
1.  **Retrieves** real facts from a trusted PDF document (Ingestion).
2.  **Augments** the AI's prompt with those specific facts.
3.  **Generates** a natural answer using the Gemini LLM.

**Status:** 🛠️ *Prototype / Proof of Concept*

## 🛠️ Tech Stack
* **Backend:** Python 3.14, FastAPI, Uvicorn
* **AI & Logic:** Google Gemini Flash (LLM), Sentence-Transformers (Embeddings), FAISS (Vector Database)
* **Frontend:** React (Vite), CSS3
* **Tools:** PDF Parsing (pypdf), Text Chunking (tiktoken)

## ⚙️ Architecture
1.  **Ingestion:** Python script reads `chennai_services.pdf` -> splits into chunks -> saves embeddings to FAISS.
2.  **Search:** User asks a question -> System finds the top 4 relevant chunks.
3.  **Answer:** Gemini API receives the User Question + Relevant Chunks -> Returns a factual answer.

## 📦 How to Run
1.  **Backend:**
    ```bash
    cd backend
    # Set your Gemini API Key first!
    python -m uvicorn main:app --reload
    ```
2.  **Frontend:**
    ```bash
    cd frontend
    npm run dev
    ```