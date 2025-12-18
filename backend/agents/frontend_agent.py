import json
import os
from backend.llm.gemini import gemini_generate


def extract_json(text: str) -> dict:
    start = text.find("{")
    end = text.rfind("}") + 1
    if start == -1 or end == -1:
        raise ValueError("No JSON found")
    return json.loads(text[start:end])


def get_file_list(instruction: str, root="frontend") -> list:
    prompt = f"""
Return ONLY valid JSON.

TASK:
Based on this instruction, list the frontend files needed.

INSTRUCTION:
{instruction}

FORMAT:
{{
  "files": [
    "{root}/index.html",
    "{root}/style.css"
  ]
}}
"""

    raw = gemini_generate(prompt)
    data = extract_json(raw)

    if "files" not in data or not data["files"]:
        raise ValueError("No files returned")

    return data["files"]


def generate_single_file(path: str, instruction: str) -> str:
    prompt = f"""
You are a senior frontend engineer.

Generate ONLY the raw content for this file:
{path}

PROJECT REQUIREMENT:
{instruction}

RULES:
- Output ONLY file content
- NO markdown
- NO explanations
"""

    content = gemini_generate(prompt)

    if not content.strip():
        raise ValueError(f"Empty content for {path}")

    return content


def write_file(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_frontend(instruction: str, root="frontend"):
    print("🟡 Agent started")

    files = get_file_list(instruction, root)
    print("📁 Files to generate:", files)

    output = []

    for path in files:
        print(f"🛠 Generating {path}")
        content = generate_single_file(path, instruction)
        write_file(path, content)

        output.append({
            "path": path,
            "content": content
        })

    print(f"🟢 Successfully generated {len(output)} files")
    return {"files": output}
