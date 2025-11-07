
from fastapi import FastAPI, HTTPException
import httpx
import asyncio

app = FastAPI(title="day-5-Async Data Fetcher API")

async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@app.get("/fetch")
async def fetch_api_data(url: str):
    """
    Fetches data from any public API asynchronously.
    Example: /fetch?url=https://api.github.com
    """ 
    try:
        data = await fetch_url(url)
        return {"fetched_from": url, "data": data}
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=str(e))