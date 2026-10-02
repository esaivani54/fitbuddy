import os
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "FitBuddy"
    APP_ENV: str = "development"
    DEBUG: bool = True
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    
    # Database
    DATABASE_URL: str = "sqlite:///./fitbuddy.db"
    
    # Google Gemini AI Config
    GEMINI_API_KEY: str = ""
    GEMINI_WORKOUT_MODEL: str = "gemini-2.5-flash"
    GEMINI_NUTRITION_MODEL: str = "gemini-2.5-flash"

    # Public URLs for Cross-Origin Hosting
    BACKEND_URL: str = ""
    FRONTEND_URL: str = ""
    
    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
