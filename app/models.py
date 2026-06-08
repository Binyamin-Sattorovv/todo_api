from sqlalchemy import String, Column, Integer, Boolean
from mini_projects.todo_api.app.database import Base


class Task(Base):
    
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    
    title = Column(String, nullable=False)
    
    completed = Column(Boolean, default=False)
    
    