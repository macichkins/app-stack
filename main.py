import os
from fastapi import FastAPI
import redis.asyncio as redis

app = FastAPI(title="ameba DevOps Backend Server")

@app.get("/")
async def root():
    return {"status": "ok", "message": "FastAPI is running on Lenovo Server!"}

@app.get("/health")
async def health_check():
    redis_url = os.getenv("REDIS_URL", "redis://cache:6379")
    r = redis.from_url(redis_url)
    ping = await r.ping()
    await r.aclose()
    
    return {
        "postgres": "connected",
        "redis_ping": ping,
        "database_url": os.getenv("DATABASE_URL")
    }


