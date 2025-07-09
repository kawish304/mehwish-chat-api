from gtts import gTTS
import uuid
import os

def generate_audio_response(text, lang="en"):
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename
  
