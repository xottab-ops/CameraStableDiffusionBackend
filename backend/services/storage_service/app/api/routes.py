from fastapi import APIRouter, UploadFile, HTTPException, Form
from services.storage import upload_image_to_s3

router = APIRouter()

@router.post("/upload")
async def upload_image(image: UploadFile, image_name: str = Form(...)):
    try:
        object_url = upload_image_to_s3(image.file, image_name)
        return {"message": "Image uploaded successfully", "image_name": image_name, "url": object_url}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")