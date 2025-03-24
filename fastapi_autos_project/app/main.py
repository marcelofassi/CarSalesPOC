from fastapi import FastAPI
from app.api import autos

app = FastAPI()

app.include_router(autos.router)
