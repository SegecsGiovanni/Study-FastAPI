from core.configs import settings
from core.database import engine

async def create_tables():
    from models import __all_models
    print("Creating database tables...")

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Database tables created successfully.")


if __name__ == "__main__":
    import asyncio
    asyncio.run(create_tables())