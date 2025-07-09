# illegal_filter.py

from fastapi import Request
from fastapi.responses import JSONResponse

# ✅ Sample multilingual illegal keywords (expandable)
illegal_keywords = {
    "en": ["bomb", "porn", "child abuse", "weapon", "kill"],
    "ur": ["بم", "فحش", "بچے کا استحصال", "ہتھیار", "قتل"],
    "hi": ["बम", "अश्लील", "बाल शोषण", "हथियार", "हत्या"],
    "ar": ["قنبلة", "إباحية", "استغلال الأطفال", "سلاح", "قتل"],
    "zh": ["炸弹", "色情", "虐待儿童", "武器", "杀人"]
    # ⚠️ You can add more languages and terms here
}

async def check_illegal_content(request: Request, body: dict):
    message = body.get("message", "").lower()

    for lang, keywords in illegal_keywords.items():
        for word in keywords:
            if word.lower() in message:
                return JSONResponse(
                    status_code=403,
                    content={"error": f"🚫 Blocked illegal term detected in {lang.upper()}"}
                )
    return None
  
