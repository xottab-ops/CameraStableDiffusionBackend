import os

class Settings:
    def __init__(self):
        self.AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', 'default')
        self.AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY', 'default')
        self.S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'default')
        self.S3_REGION = os.getenv('S3_REGION', 'ru-central1')
        self.S3_ENDPOINT = os.getenv('S3_ENDPOINT', 'https://storage.yandexcloud.net')
        self.STORAGE_SERVICE_PORT = os.getenv('STORAGE_SERVICE_PORT', 5000)
        self.STORAGE_SERVICE_LISTEN_ADDRESS = os.getenv('QR_GENERATOR_LISTEN_ADDRESS', '0.0.0.0')

settings = Settings()