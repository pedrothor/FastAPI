from typing import List, ClassVar

from pydantic_settings import BaseSettings

from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade'
    DBBaseModel: ClassVar = declarative_base()

    JWT_SECRET: str = 'KPPu21zlKeKuT9Uyy4HYKKtKDdXoXxfV-Lp-i9qDrdQ'
    """
        # biblioteca interna do python para gerar códigos
        
        import secrets
        token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'

    # 60 minutos * 24 horas * 7 dias = 1 semana (podemos colocar qualquer tempo em minutos para expirar o token)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive=True

settings: Settings = Settings()
