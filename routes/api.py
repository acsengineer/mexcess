from fastapi import APIRouter

from endpoints import excess


router = APIRouter()
router.include_router(excess.router)
