import asyncpg
import os

_pool=None

async def get_pool():
    global pool
    if _pool is None:
        _pool=await asyncpg.create_pool(
            host="postgres",
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD")
        )
    return _pool

async def get_db():
    pool=await get_pool()
    async with pool.acquire() as connection:
        yield connection
    