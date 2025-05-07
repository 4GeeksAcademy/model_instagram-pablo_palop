from typing import List, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import db

if TYPE_CHECKING:
    from models import Post

media_type = Enum("media_type", "image", "video", "audio")

class Media(db.Model):
    __tablename__ = "medias"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(media_type, unique=True, nullable=False)
    url: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    
    post: Mapped[List["Post"]] = relationship("Post", back_populates="medias")