from typing import List, TYPE_CHECKING
from sqlalchemy import DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import db


if TYPE_CHECKING:
    from .users import User
    from .medias import Media

class Post(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    author_id: Mapped[List["User"]] = relationship("User", back_populates="posts")
    media_id: Mapped[List["Media"]] = relationship("Media", back_populates="posts")
    author: Mapped["User"] = mapped_column(ForeignKey("users.id"), nullable=False)