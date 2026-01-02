# fastapi 
from fastapi import APIRouter, Depends

# sqlalchemy
from sqlalchemy.orm import Session

from core.database import SessionLocal
from models.todo import Todo
from schemas.todo import TodoCreate, TodoList


router = APIRouter(
    prefix="/todos",
    tags=['Todo']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.post("/create", response_model=TodoList)
def create_todo(data: TodoCreate, db: Session = Depends(get_db)):
    todo = Todo(title=data.title)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@router.get("/list", response_model=list[TodoList])
def list_todo(db: Session = Depends(get_db)):
    return db.query(Todo).all()
