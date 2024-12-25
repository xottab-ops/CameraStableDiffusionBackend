from fastapi import FastAPI
from api.routes import router
from core.config import settings

# Initialize FastAPI app
app = FastAPI(
    title="QR Service",
    description="A microservice for generating QR codes"
)

# Include the router
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.QR_GENERATOR_LISTEN_ADDRESS, port=settings.QR_GENERATOR_PORT)

