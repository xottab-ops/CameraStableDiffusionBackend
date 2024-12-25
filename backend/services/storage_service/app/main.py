from fastapi import FastAPI
from api.routes import router
from core.config import settings

app = FastAPI(title="Storage Service")

# Подключение маршрутов
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.STORAGE_SERVICE_PORT)