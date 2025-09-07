from fastapi import FastAPI, APIRouter, Request
from .limiter import limiter
#from ..database.db import get_session
#from ..models.test_models import *

app=FastAPI()
router=APIRouter(prefix="/test",tags=["test"])

@router.get("/")
@limiter.limit("1/second")
async def test(request:Request):
    return {"message":"Test successful"}