import json
import re

def clean_and_parse_gemini_response(response_text):
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", response_text.strip(), flags=re.IGNORECASE)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print("❌ JSON Decode Error:", e)
        print("🔍 Cleaned Response:\n", cleaned)
        return None