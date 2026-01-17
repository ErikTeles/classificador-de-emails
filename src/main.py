from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil, os
import json

from src.services.PdfReaderService import read_pdf
from src.services.LLMService import classify_email_stream

BASE_DIR = Path(__file__).resolve().parent.parent
TMP_DIR = BASE_DIR / "tmp"
TMP_DIR.mkdir(exist_ok=True)

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "src/static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.get("/", response_class=HTMLResponse)
def index():
    with open(BASE_DIR / "src/templates/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/upload")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    temp_file_path = TMP_DIR / pdf_file.filename

    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(pdf_file.file, buffer)

    text = read_pdf(temp_file_path)
    result = classify_email_stream(text)

    os.remove(temp_file_path)

    return {
        "filename": pdf_file.filename,
        "response": json.loads(result)
    }