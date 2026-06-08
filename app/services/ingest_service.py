"""
  Runs the full injestion pipeline when /ingest is called
    - i.e. 
        - fetch raw articles
        - break into chunks
        - embed
        - push the vectors into Chroma
        - save the human readable metadata to SQLite
"""