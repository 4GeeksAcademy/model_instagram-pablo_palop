from typing import List
from sqlalchemy import String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import db, Post, Comment, Follower


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    posts: Mapped[List["Post"]] = relationship("Post", back_populates="users")
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="users")
    following_assoc: Mapped[List["Follower"]] = relationship(
        back_populates="user_from",
        foreign_keys="[Follower.user_from_id]",
        cascade="all, delete-orphan"
    )
    followers_assoc: Mapped[List["Follower"]] = relationship(
        back_populates="user_to",
        foreign_keys="[Follower.user_to_id]",
        cascade="all, delete-orphan"
    )
    following: Mapped[List["User"]] = relationship(
        "User",
        secondary="followers",
        primaryjoin="User.id==Follower.user_from_id",
        secondaryjoin="User.id==Follower.user_to_id",
        backref="followers",
        overlaps="following_assoc,followers_assoc"
    )