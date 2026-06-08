"""
  chain.py
    - Assembles the full pipeline using LangChain's LCEL (LangChain Expression Language). It wires together: retrieve relevant chunks from the vectorstore → format them into a prompt → send to the LLM → return the answer. LCEL lets you compose these steps with | pipes, so the chain reads almost like a data-flow diagram.
"""