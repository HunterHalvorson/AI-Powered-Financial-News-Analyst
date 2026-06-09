"""
  models.py
    - defines the structure of SQLite database tables as Python classes
"""
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.orm import declarative_base

# creates a base class that the model inherits from, SQLAlchemy uses it to track all your table definitions
Base = declarative_base()

# defines your articles table as a python class
# inheriting from Base tells SQLAlchemy this is a database table
class Article(Base):
  # names the table
  __tablename__ = "articles"
  # every row needs a unique identifier., primary_key=True means SQLAlchemy auto-increments this number for each new article.
  id = Column(Integer, primary_key=True)
  #  stores the article title as text. nullable=False means this field is required — you can't insert an article without a title.
  title = Column(String, nullable=False)
  # stores where the article came from, like "Reuters" or "Bloomberg".
  source = Column(String, nullable=False)
  # stores when the article was published as a date and time.
  published_at = Column(DateTime, nullable=False)
  #  stores the link to the full article, used later for citation cards in the UI.
  url = Column(String, nullable=False)
  ticker = Column(String, nullable=False)