from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import get_db
from schemas import TaskCreate, TaskUpdate, TaskResponse
from models import Task
from crud import create_task, delete_crud_task, update_task, get_tasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.post("/tasks")
def create_new_task(task: TaskCreate, db: Session=Depends(get_db) ):
    
    return create_task(db, task.title)


@app.get("/tasks")
def read_tasks(db: Session=Depends(get_db)):
    
    return get_tasks(db)


@app.put("/tasks/{task_id}")
def update_tasks(task_id: int, task: TaskUpdate, db: Session=Depends(get_db)):
    
    result = update_task(db, task_id, task.completed)
    print("UPDATE WORKS", task_id, task.completed)
    
    if not result:
        
        raise HTTPException(status_code=404, detail=("Task not found"))
    
    return result


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session=Depends(get_db)):
    
    task = delete_crud_task(db, task_id)
    
    if not task:
        
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"Message", "Task deleted"}




