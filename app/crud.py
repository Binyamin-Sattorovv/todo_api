from sqlalchemy.orm import Session

from mini_projects.todo_api.app.models import Task

def create_task(db: Session, title: str):
    
    task = Task(title=title)
    
    db.add(task)
    
    db.commit()
    
    db.refresh(task)
    
    return task


def get_tasks(db: Session):
    
    return db.query(Task).all()


def update_task(db: Session, task_id: int, completed: bool):
    
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if not task:
        
        return None
    
    task.completed = completed
    
    db.commit()
    
    db.refresh(task)
    
    return task


def delete_crud_task(db: Session, task_id: int):
    
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if not task:
        
        return None
    
    db.delete(task)
    
    db.commit()
    
    return True