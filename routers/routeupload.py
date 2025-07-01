from fastapi import APIRouter,File,UploadFile
from typing import Annotated

from schemas.navroute import NavRoute
from services.route_services import parse_route

router = APIRouter()

@router.post("/routes/")
async def upload_and_convert_route(route_file:Annotated[UploadFile,File()])->NavRoute|bool:
    route_file_name = route_file.filename
    parsing_result = parse_route(route_file=await route_file.read(),route_file_name=route_file_name)
    return parsing_result