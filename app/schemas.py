from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    
    title: str = Field(..., description="Task")
    


class TaskResponse(BaseModel):
    
    id: int = Field(..., description="Id")
    
    title: str = Field(..., description="Title")
    
    completed: bool
    
    
    class Config:
        
        form_attribbutes = True
        
        

class TaskUpdate(BaseModel):
    
    completed: bool
    