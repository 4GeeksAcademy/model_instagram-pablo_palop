from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import db

if TYPE_CHECKING:
    from models import User


class Follower(db.Model):
    __tablename__ = "followers"
    user_from_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)

    user_from: Mapped["User"] = relationship(
        back_populates="following_assoc",
        foreign_keys=[user_from_id]
    )
    user_to: Mapped["User"] = relationship(
        back_populates="followers_assoc",
        foreign_keys=[user_to_id]
    )