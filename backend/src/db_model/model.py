from datetime import datetime, timezone

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship, query
from sqlalchemy import Text, ForeignKey, DateTime, String, func, UniqueConstraint


class Datasets(Base):
    __tablename__ = 'dataset'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    path: Mapped[str] = mapped_column(unique=True)
    type: Mapped[str]
    UniqueConstraint('path', name='uc_path')