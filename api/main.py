from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routes.test import router as test_router


router=APIRouter()
app=FastAPI()

app.include_router(test_router)


