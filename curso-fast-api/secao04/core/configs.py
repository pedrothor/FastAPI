# através no pydantic é possível criar uma estrutura semelhante à do arquivo settings.py (do django)

import typing
from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):

    # configurações gerais usadas na aplicação

    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade"
    DBBaseModel: typing.ClassVar = declarative_base()

    class Config:
        # manter se for maiúsculo ou se for minúsculo
        case_sensitive = True

settings = Settings()