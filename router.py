from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, StaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)
@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> StaskId:
    task_id = await TaskRepository.add_one(task)
    return{"ok": True, "task_id": task_id}

@router.get("/tasks")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
