from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/QR")
def generate_qr(form_id: int, q: Optional[str] = None):
    return FileResponse("example.jpg")
