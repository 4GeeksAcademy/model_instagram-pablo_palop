from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import db

if TYPE_CHECKING:
    from .posts import Post


class Media(db.Model):
    __tablename__ = "medias"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    url: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    
    post: Mapped["Post"] = relationship("Post", back_populates="media")
