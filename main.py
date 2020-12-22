import io
from typing import Optional

import qrcode
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/QR")
def generate_qr(form_id: int, q: Optional[str] = None):
    # Create instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    # Give parameter from GET
    qr.add_data(form_id)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    # Buffer to save the image on RAM
    buffer = io.BytesIO()
    img.save(buffer, "PNG")
    response_img = buffer.getvalue()
    # Return QR code as image
    return Response(content=response_img, media_type="image/png")
