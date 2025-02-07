import os
from fastapi import FastAPI
import pydantic

from app import Hello

app = FastAPI()

@app.get("/")
async def root():
    return {"message: Hello World!"}