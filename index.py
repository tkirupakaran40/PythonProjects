from fastapi import FastAPI
 
from config.routes.index import vehicle

app = FastAPI()

app.include_router(vehicle)

