from pathlib import Path

def write_file(path: str, content: str) -> None:
    file_path = Path(path)
    file_path.write_text(content, encoding="utf-8")
