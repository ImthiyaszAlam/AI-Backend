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
        response = await client.post(url,headers=headers,json=data)
        if response.status_code !=200 :
            raise HTTPException (status_code=response.status_code,detail=response.text)
        return response.json()["choices"][0]["message"]["content"]
    

    @app.post("/chat")
    async def chat(request:ChatRequest):
        try:
            reply = await call_open_ai(request.message)
            return {"user_message": request.message, "ai_reply": reply}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


