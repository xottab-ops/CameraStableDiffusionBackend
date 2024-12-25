from botocore.exceptions import BotoCoreError, ClientError
from core.s3_client import get_s3_client
from core.config import settings
import logging

logger = logging.getLogger(__name__)
s3_client = get_s3_client()

def upload_image_to_s3(image_file, image_name: str) -> str:
    try:
        s3_client.upload_fileobj(image_file, settings.S3_BUCKET_NAME, image_name)
        object_url = f"{settings.S3_ENDPOINT}/{settings.S3_BUCKET_NAME}/{image_name}"
        logger.info(f"Image '{image_name}' successfully uploaded to S3: {object_url}")
        return object_url
    except (BotoCoreError, ClientError) as e:
        logger.error(f"Failed to upload image to S3: {str(e)}")
        raise RuntimeError("Failed to upload image to S3")