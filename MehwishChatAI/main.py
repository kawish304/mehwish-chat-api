from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from illegal_filter import check_illegal_content
from gtts import gTTS
import uuid
import os

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: Request):
    body = await request.json()

    # Illegal content filter
    block_response = await check_illegal_content(request, body)
    if block_response:
        return block_response

    message = body.get("message", "")
    reply_text = f"✅ Mehwish AI received: {message}"

    # Generate unique audio filename
    audio_filename = f"response_{uuid.uuid4().hex}.mp3"
    tts = gTTS(reply_text, lang='en')
    tts.save(audio_filename)

    return JSONResponse(content={
        "response": reply_text,
        "audio_url": f"/audio/{audio_filename}"
    })

# Serve audio files
from fastapi.staticfiles import StaticFiles
app.mount("/audio", StaticFiles(directory="."), name="audio")
