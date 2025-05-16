from typing import List, TYPE_CHECKING
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, ForeignKey
from .database import db


if TYPE_CHECKING:
    from models import User, Media

class Post(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    author_id: Mapped[List["User"]] = relationship("User", back_populates="posts")
    media_id: Mapped[List["Media"]] = relationship("Media", back_populates="posts")
    author: Mapped["User"] = mapped_column(ForeignKey("users.id"), nullable=False)