from sqlalchemy.orm import sessionmaker, AsyncEngine, AsyncSession

from core.configs import settings

engine: AsyncEngine = AsyncEngine(settings.DB_URL)


Session: AsyncSession = sessionmaker(
    autocommit = False,
    autoflush = False,
    expire_on_commit = False,
    class_ = AsyncSession,
    bind = engine
)