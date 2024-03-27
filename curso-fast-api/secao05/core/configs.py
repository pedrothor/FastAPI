from pydantic_settings import BaseSettings
from typing import ClassVar

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: ClassVar = 'postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade'

    class Config:
        case_sensitive = True

settings: Settings = Settings()
