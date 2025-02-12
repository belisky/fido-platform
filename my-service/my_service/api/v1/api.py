# app/api/api_v1/api.py
from fastapi import APIRouter

from my_service.api.v1.routers import argocd_querier_router

router = APIRouter(prefix="/api/v1")
router.include_router(argocd_querier_router.router)
