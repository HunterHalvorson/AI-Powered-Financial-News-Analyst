"""
  embedder.py
    - Wraps sentence-transformers to convert text into vector embeddings
"""
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str):
  return model.encode(text).tolist()

