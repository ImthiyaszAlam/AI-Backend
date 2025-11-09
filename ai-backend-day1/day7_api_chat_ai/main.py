from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv



load_dotenv()

OPEN_API_KEY = os.getenv
app = FastAPI(title="Day 7 - AI Chat API")


async def call_open_ai(prompt:str):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
         "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data={
         "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    async with httpx.AsyncClient(timeout=10.0) as client:
