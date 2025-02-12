from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
    BACKEND_ORIGINS: List[AnyHttpUrl] = []
    FASTAPI_PROJECT_NAME: str = "my-service"
    LOG_LEVEL: str = "DEBUG"

    # ArgoCD Config defaults
    ARGOCD_SERVER: str = "localhost"
    ARGOCD_PORT: str = "<ARGOCD_PORT>"
    ARGOCD_URL: str = f"{ARGOCD_SERVER}:{ARGOCD_PORT}"
    ARGOCD_PASSWORD: str = "<ARGOCD_ADMIN_USER_PASSWORD>"
    ARGOCD_USERNAME: str = "admin"                              # default argocd user
    TOKEN_CACHE_TTL: int = 600

    model_config = SettingsConfigDict(env_nested_delimiter='__')


settings = Settings(_env_file=".env")
