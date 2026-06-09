"""
  config.py: needs to do one thing: load your API keys from .envfile so that the rest of the app can use them

  - The app needs api keys to talk to newAPI and OpenAI
  - These keys are in the .env, config is the one place they are loaded
    into the app
"""

# imports the tool that handles reading env variables and validating them
from pydantic_settings import BaseSettings

# inheriting meanspydantic knows how to look for these values in the .env file
class Settings(BaseSettings):
  # no default means the app crashes if not provided
  newsapi_key: str
  openai_api_key: str

  # inner class that passes configuration options to BaseSettings.
  class Config:
    env_file = ".env"


# creates one instance of the class, which triggers pydantic
# to actually read the .env file right now.
# Every other file imports this object instead of creating their own
settings = Settings()
