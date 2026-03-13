import redis.asyncio as redis
import os,json

_client=None

async def get_client():
    global _client
    if _client is None:
        _client=redis.from_url(
            os.getenv(
            "REDIS_URL","redis://redis:6379"
            )
        )
    return _client

async def get_data(key: str):
    client=await get_client()
    data=client.get(key)
    return json.loads(data)

async def catch_set(key:str,value:dict,ttl:int=3600):
    client=await get_client()
    client.setex(key,ttl,json.dump(value))

async def catch_delete(key:str):
    client=await get_client()
    await client.delete(key)
