from pathlib import Path

def read_file(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return file_path.read_text(encoding="utf-8")
