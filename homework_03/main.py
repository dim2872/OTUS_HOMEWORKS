import uvicorn
from fastapi import FastAPI, Body, Depends, Query

app = FastAPI()


@app.get("/ping/")
def read_root():
    return {"message": "pong"}
