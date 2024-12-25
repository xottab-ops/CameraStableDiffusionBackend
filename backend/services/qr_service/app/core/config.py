import os

class Settings:
    def __init__(self):
        self.QR_GENERATOR_PORT = os.getenv('QR_GENERATOR_PORT', 6000)
        self.QR_GENERATOR_LISTEN_ADDRESS = os.getenv('QR_GENERATOR_LISTEN_ADDRESS', '0.0.0.0')

settings = Settings()