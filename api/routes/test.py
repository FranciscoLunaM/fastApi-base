from fastapi import FastAPI, APIRouter
#from ..database.db import get_session
#from ..models.test_models import *

app=FastAPI()
router=APIRouter(prefix="/test",tags=["test"])

@router.get("/")
async def test():
    return {"message":"Test successful"}