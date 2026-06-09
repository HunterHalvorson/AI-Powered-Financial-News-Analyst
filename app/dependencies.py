"""
  dependencies.py
    - It creates shared resources that your routes need and hands them out per request.
    - The main one right now is the database session — every request that touches the database needs a session opened at the start and closed at the end. Instead of every route function creating its own session, dependencies.py defines that logic once and FastAPI injects it automatically wherever it's needed.

    https://docs.sqlalchemy.org/en/21/core/engines.html
"""

# factory that sets up a connection to the database
# create_engine, does not connect immediately its LAZY, it doesnt open up a 
# conenction, it just stores the configuration and prepares a connection pool
from sqlalchemy import create_engine
from app.config import settings
"""
  factory that creates session classes, this is the main tool for communicating
  with a database in sqlalchemy.

  The "what is a Session?" part first
    A Session is like a scratchpad or shopping cart for database operations. You stage your changes (add, update, delete) and then either commit them (save to DB) or rollback (throw them away). Nothing hits the real database until you say so.
  
  What sessionmaker does
    Rather than configuring a Session from scratch every time, sessionmaker lets you pre-bake a Session class with your settings once:
  
  So what is sessionmaker?
    - "set up my sessions to always use this database"
"""
from sqlalchemy.orm import sessionmaker

# create engine (db connection).  
engine = create_engine(settings.sqlite_url)

"""
  autocommit=False, Don't automatically save changes to the DB. You have to manually call session.commit() yourself

  autoflush=False, Don't automatically sync your staged changes to the DB before every query
"""
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
  # new session
  db = SessionLocal()
  try:
    # gives to whoever asked for it, (pauses here while it is used)
    yield db 
  finally:
    # once they're done, close it automatically
    db.close()