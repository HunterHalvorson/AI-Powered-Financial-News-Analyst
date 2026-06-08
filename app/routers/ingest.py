"""
  ingest.py -- POST/ingest
    - Triggers the news ingestion pipeline on demand

    1. fetch articles from NewsAPI for this ticker
    2. chunk + embed + store in Chroma
    3. save metadata to SQLite
"""