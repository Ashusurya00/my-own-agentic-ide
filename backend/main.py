from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel

from backend.agents.editor import generate_files
from backend.tools.file_creator import create_files

app = FastAPI()



class GenerateRequest(BaseModel):
    instruction: str
    root: str = "frontend"


@app.post("/generate")
def generate(req: GenerateRequest):
    try:
        result = generate_files(req.instruction, req.root)
        created = create_files(result["files"])

        if not created:
            raise RuntimeError("No files were written to disk")

        return {
            "status": "success",
            "message": "Files created",
            "files": created
        }

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {
            "status": "error",
            "message": str(e)
        }
