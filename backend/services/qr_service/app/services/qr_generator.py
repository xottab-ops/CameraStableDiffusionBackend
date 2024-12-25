import io
import qrcode
from PIL import Image

def generate_qr_code(link: str) -> bytes:
    """
    Generates a QR code for a given URL.
    :param link: The URL to encode in the QR code.
    :return: Binary representation of the QR code in PNG format.
    """
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer.read()