# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Backend"
    environment: str = "dev"
    default_url: str = "https://httpbin.org/get"

    class Config:
        env_file = ".env"

settings = Settings()
