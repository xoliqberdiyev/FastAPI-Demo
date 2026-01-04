from fastapi import FastAPI

from core.database import Base, engine
from routers.todo import router

app = FastAPI(
    title="Todo API",
)

app.include_router(router)
