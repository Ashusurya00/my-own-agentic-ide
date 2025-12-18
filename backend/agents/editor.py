import json
import re
from backend.llm.gemini import gemini_generate


def extract_json(text: str) -> str:
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON found")
    return match.group(0)


def generate_files(instruction: str, root: str = "frontend", max_retries: int = 2):
    print("🟡 Agent started")

    base_prompt = f"""
You are a JSON generator.

STRICT RULES:
- Output ONLY valid JSON
- No markdown
- No explanations
- Escape all newlines as \\n
- Escape quotes properly
- NEVER truncate output

TASK:
{instruction}

OUTPUT FORMAT:
{{
  "files": [
    {{
      "path": "{root}/index.html",
      "content": "..."
    }}
  ]
}}
"""

    last_error = None

    for attempt in range(1, max_retries + 1):
        print(f"🔁 Attempt {attempt}")

        raw = gemini_generate(base_prompt)

        print("🔍 RAW RESPONSE:\n", raw)

        try:
            json_text = extract_json(raw)
            data = json.loads(json_text)

            # HARD VALIDATION
            if "files" not in data or not data["files"]:
                raise ValueError("No files returned")

            for f in data["files"]:
                if "path" not in f or "content" not in f:
                    raise ValueError("Invalid file object")

            print(f"🟢 Valid files received: {len(data['files'])}")
            return data

        except Exception as e:
            print("❌ Parse failed:", e)
            last_error = e

            # 🔧 SELF-REPAIR PROMPT
            base_prompt = f"""
The previous response was INVALID or TRUNCATED JSON.

ERROR:
{e}

FIX IT.
Return COMPLETE and VALID JSON ONLY.

Original task:
{instruction}
"""

    raise RuntimeError(f"LLM failed after {max_retries} attempts") from last_error
