from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class Todo(Base):
    __tablename__ = "todos"
    
    title: Mapped[str] = mapped_column(String(200))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

    