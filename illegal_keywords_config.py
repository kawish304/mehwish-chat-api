# language_config.py
# 🧠 Multilingual Config for Kawish API (Created by Syed Kawish Ali)

SUPPORTED_LANGUAGES = {
    "en": "English",
    "ur": "Urdu",
    "hi": "Hindi",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "ru": "Russian",
    "pt": "Portuguese",
    "tr": "Turkish",
    "ja": "Japanese",
    "ko": "Korean",
    "it": "Italian",
    "bn": "Bengali",
    "pa": "Punjabi",
    "fa": "Persian",
    "sw": "Swahili",
    "th": "Thai",
    "id": "Indonesian",
    "ta": "Tamil",
    "te": "Telugu"
}

def get_language_label(lang_code: str) -> str:
    return SUPPORTED_LANGUAGES.get(lang_code, "Unsupported Language")
  
