import uvicorn as uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from my_service.config.config import settings
from my_service.models.models import HealthCheckResponse
from my_service.utils.logger import setup_logger
from my_service.api.v1 import api


logger = setup_logger()
logger.debug(f"Running with config: {settings}")


def get_applcation():
    _app = FastAPI(title=settings.FASTAPI_PROJECT_NAME)  
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    return _app


app = get_applcation()
app.include_router(api.router)


@app.get("/healthcheck")
async def healthcheck() -> HealthCheckResponse:
    logger.debug("healthcheck hit")
    return HealthCheckResponse(
        status_code=status.HTTP_200_OK,
        message="Server is runing!"
    )


if __name__ == "__main__":
    uvicorn.run("my_service.main:app", port=9000)
