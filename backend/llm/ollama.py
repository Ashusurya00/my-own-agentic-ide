import requests
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-coder"   # ✅ IMPORTANT


def ollama_generate(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    text = response.json()["response"]

    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("Model did not return valid JSON")

    return match.group(0)
