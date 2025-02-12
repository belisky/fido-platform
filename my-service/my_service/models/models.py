from pydantic import BaseModel
from typing import Dict, List, Optional


class HealthCheckResponse(BaseModel):
    status_code: int
    message: str


class ArgoCDCreds(BaseModel):
    username: str
    password: str
