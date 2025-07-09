from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uuid
from datetime import datetime, timedelta
import asyncio

app = FastAPI()

# Generate API key
async def generate_key():
    await asyncio.sleep(0.5)
    return str(uuid.uuid4())

@app.get("/generate-key")
async def get_key():
    key = await generate_key()
    expiry = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    return {"api_key": key, "expiry": expiry}

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        message = data.get("message", "")
        reply = f"Kawish Super Power AI received: {message}"
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
