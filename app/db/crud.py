"""
  Contains the actual database operations, keeping them seperate from your models and routes. (CREATE, READ, UPDATE, DELETE)
"""

from sqlalchemy.orm import Session 
from app.db.models import Article

# function to insert an article
def insert_article(db: Session, title: str, source: str, published_at, url: str, ticker: str):
  # creates a new article object in memory
  article = Article(title=title, source=source, published_at=published_at, url=url, ticker=ticker)
  # adds the article to the session (still has not hit the database)
  db.add(article)
  # saves everything from the session to the db
  db.commit()
  # after committing, SQLAlchemy refreshes the object from the database so it has the auto-generated id value. Without this the id field would still be empty.
  db.refresh(article)
  # returns the saved article object with its new id included.
  return article

"""
  Notes:
    - Session: You never talk to the database directly — you talk to the session and the session talks to the database. The reason it gets passed in as a parameter instead of created inside the function is so that one session can be shared across multiple operations in the same request
  
    - Refresh: When you commit an article, SQLite generates the id automatically. But your Python article object was created before that happened, so it doesn't know what id it got. db.refresh(article) goes back to the database and syncs the object with what's actually stored — so now your article object has the real id on it.
"""


def get_articles(db: Session, ticker: str) -> list[Article]:
  """
    db.query(Article): same as saying SELECT * FROM articles.
    .filter(Article.ticker == ticker): narrows it down to only rows where the ticker column matches what was passed in. Equivalent to WHERE ticker = 'AAPL'
    .all(): executes the query and returns all matching rows as a list
  """
  return db.query(Article).filter(Article.ticker == ticker).all()
