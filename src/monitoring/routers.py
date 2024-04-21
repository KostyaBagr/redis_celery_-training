from fastapi import APIRouter

router = APIRouter() 

@router.get("/test_start")
async def start():
    return {"hello": "start"}