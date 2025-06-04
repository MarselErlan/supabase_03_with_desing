import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):

    POSTGRES_URI: str = os.getenv("POSTGRES_URI")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

if not settings.POSTGRES_URI:
    raise ValueError("POSTGRES_URI is required in .env")