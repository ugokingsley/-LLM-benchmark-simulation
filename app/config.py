# app/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str

    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra fields


settings = Settings()
