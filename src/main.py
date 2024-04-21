from fastapi import APIRouter, FastAPI
from monitoring.routers import router


app = FastAPI()
app.include_router(router=router)