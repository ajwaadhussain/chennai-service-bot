import tiktoken
from typing import List

def chunk_text(text: str, chunk_tokens: int = 450, overlap_tokens: int = 80) -> List[str]:
    # This matches the tokenizer used by OpenAI's newer models
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)

    chunks = []
    start = 0
    while start < len(tokens):
        end = start + chunk_tokens
        # Decode the tokens back into text
        chunk = enc.decode(tokens[start:end])
        chunks.append(chunk)
        # Move forward, but keep an overlap so we don't cut sentences in half
        start = end - overlap_tokens
        if start < 0:
            start = 0
            
    return chunks

if __name__ == "__main__":
    # Test it
    test_text = "Chennai is the capital of Tamil Nadu. " * 50
    print(chunk_text(test_text, chunk_tokens=20, overlap_tokens=5))