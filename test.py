from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Task(BaseModel):
    name: str
    description: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Server is working"}

@app.get("/taskss")
def get_tasks():
    task = Task(name="Запиши эту запись")
    return {"data": task}
