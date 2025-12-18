from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def create_files(files: list[dict]):
    created = []

    print("📍 Current Working Directory:", os.getcwd())
    print("📍 Project Root:", PROJECT_ROOT)

    for f in files:
        absolute_path = PROJECT_ROOT / f["path"]
        absolute_path.parent.mkdir(parents=True, exist_ok=True)
        absolute_path.write_text(f["content"], encoding="utf-8")

        print("📁 FILE CREATED AT:", absolute_path)
        created.append(str(absolute_path))

    return created
