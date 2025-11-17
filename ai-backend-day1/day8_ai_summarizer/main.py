from fastapi import FastAPI
from pydantic import BaseModel
import httpx, os
from dotenv import load_doten

app = FastAPI(title="DAY-8 AI Summarizer")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

class SummaryRequest(BaseModel):
    text:str

    @app.post("/summarize")
    async def summarize(request:SummaryRequest):
        async with httpx.AsyncClient() as client :
            response = await client.post("https://api.openai.com/v1/chat/completions",
                                         headers={
                                              "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
                                         },
                                         json="model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a professional text summarizer."},
                    {"role": "user", "content": f"Summarize this: {request.text}"}
                ])
            data = response.json
