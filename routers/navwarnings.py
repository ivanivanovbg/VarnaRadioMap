from fastapi import APIRouter
from typing import List
from schemas.navwarn import NavWarning
from services.navwarnings_services import get_all_warnings_service

router = APIRouter(prefix="/navwarnings")

@router.get("/")
async def get_all_warnings()->List[NavWarning]|None:
    nav_warnings = await get_all_warnings_service()
    return nav_warnings