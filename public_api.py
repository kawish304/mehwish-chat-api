from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from illegal_filter import check_illegal_content
from gtts import gTTS
import uuid
import os

app = FastAPI(
    title="Kawish Public API",
    description="✅ Super Power AI API with Halal & Legal Filters — Created by Syed Kawish Ali",
    version="1.0.0"
)

@app.post("/public-chat")
async def public_chat(request: Request):
    body = await request.json()
    
    # ✅ Illegal Content Blocker
    block_response = await check_illegal_content(request, body)
    if block_response:
        return block_response

    message = body.get("message", "")
    response_text = f"✅ Kawish Public AI says: {message}"

    # 🎧 Generate Audio Response
    audio_filename = f"public_{uuid.uuid4().hex}.mp3"
    tts = gTTS(response_text, lang='en')
    tts.save(audio_filename)

    return JSONResponse(content={
        "response": response_text,
        "audio_url": f"/audio/{audio_filename}"
    })

# 🎧 Serve Audio Files
from fastapi.staticfiles import StaticFiles
app.mount("/audio", StaticFiles(directory="."), name="audio")
