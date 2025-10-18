from typing import List, Any

# pydantic v2 mudou o BaseSettings para o pacote pydantic-settings
from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base

# keep the declarative base at module level so other modules can import it
DBBaseModel = declarative_base()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://geek:734327_Segecs@localhost:5432/faculdade"
    # campo opcional para compatibilidade com código legado que espera
    # acessar `settings.DBBaseModel`.
    DBBaseModel: Any | None = None

    JWT_SECRET: str = 'tVl8yRgF4WxarPa7MExNqrWBirDdVTDmPfeKN0Sx5_s'
    """ on terminal**
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = "HS256"

    # 60min x 24h x 7d = 1sem
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


# instantiate settings and expose DBBaseModel through settings for backward compatibility
settings: Settings = Settings()
settings.DBBaseModel = DBBaseModel