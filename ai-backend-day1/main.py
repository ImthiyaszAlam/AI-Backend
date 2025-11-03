# main.py
from fastapi import FastAPI, Query
import asyncio
from mini_logger import MiniLogger
from api_caller_async import fetch
from config import settings

logger = MiniLogger("FastAPI")
app = FastAPI(title=settings.app_name)

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.app_name} in {settings.environment} mode")

@app.get("/ping")
async def ping():
    return {"status": "ok", "app": settings.app_name}

@app.get("/fetch")
async def fetch_data(url: str = Query(default=settings.default_url)):
    logger.info(f"Fetching URL: {url}")
    result = await fetch(url)
    return {"success": result is not None, "data": result}
