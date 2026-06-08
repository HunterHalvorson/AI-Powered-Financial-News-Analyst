financial-news-analyst/
│
├── app/                          # Backend package
│   ├── __init__.py
│   ├── main.py                   # FastAPI app entry point + CORS
│   ├── config.py                 # Environment variables via pydantic-settings
│   ├── dependencies.py           # Shared dependencies (DB session, Chroma, chain)
│   │
│   ├── routers/                  # HTTP endpoints
│   │   ├── __init__.py
│   │   ├── query.py              # POST /query
│   │   ├── ingest.py             # POST /ingest
│   │   └── summary.py            # GET /summary (stretch goal)
│   │
│   ├── schemas/                  # Pydantic request / response models
│   │   ├── __init__.py
│   │   ├── query.py              # QueryRequest / QueryResponse / SourceCitation
│   │   └── article.py            # ArticleMetadata
│   │
│   ├── services/                 # Business logic
│   │   ├── __init__.py
│   │   ├── ingest_service.py     # fetch → chunk → embed → store
│   │   └── rag_service.py        # LCEL chain: retrieve → LLM → response
│   │
│   ├── db/                       # SQLite
│   │   ├── __init__.py
│   │   ├── models.py             # Article SQLAlchemy model
│   │   └── crud.py               # Insert / query helpers
│   │
│   └── rag/                      # RAG pipeline
│       ├── __init__.py
│       ├── embedder.py           # sentence-transformers wrapper
│       ├── vectorstore.py        # Chroma init + retrieval
│       └── chain.py              # LangChain LCEL chain definition
│
├── frontend/                     # React + Vite + Tailwind
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatThread.jsx    # Message history
│   │   │   ├── MessageInput.jsx  # Text input + send
│   │   │   ├── SourceCard.jsx    # Citation cards
│   │   │   └── TickerSelector.jsx # Knowledge base switcher
│   │   ├── api/
│   │   │   └── client.js         # fetch wrappers for FastAPI
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── scripts/                      # Standalone runners
│   ├── ingest_news.py            # Run manually or triggered via /ingest
│   └── seed_chroma.py            # One-time vector store seed
│
├── tests/                        # pytest
│   ├── test_ingest.py
│   └── test_query.py
│
├── chroma_db/                    # Gitignored — Chroma persisted data
│
├── .env                          # API keys — never commit
├── .env.example                  # Template to commit
├── .gitignore
├── requirements.txt
└── README.md