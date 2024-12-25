from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from logging import getLogger
from services.qr_generator import generate_qr_code
from fastapi.responses import StreamingResponse
import io

logger = getLogger("qr_service")
router = APIRouter()

class LinkRequest(BaseModel):
    url: HttpUrl

class QRResponse(BaseModel):
    url: HttpUrl
    qr_code: str

@router.post("/generate_qr")
async def generate_qr(link_request: LinkRequest):
    """
    Endpoint to generate a QR code for a given URL.
    :param link_request: The URL to encode in the QR code.
    :return: The original URL and the QR code as a PNG image.
    """
    try:
        link = link_request.url
        logger.info(f"Received request to generate QR code for: {link}")
        qr_code = generate_qr_code(link)

        return StreamingResponse(io.BytesIO(qr_code), media_type="image/png", headers={
            "X-Original-URL": str(link),
            "Content-Disposition": "inline; filename=qr_code.png"
        })
    except Exception as e:
        logger.error(f"Error generating QR code: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate QR code")