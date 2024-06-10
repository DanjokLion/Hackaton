from sqlalchemy import   String, Text, Date, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship, query
from src.database import Base
from datetime import date
from typing import Any


class Patents(Base):
    __tablename__ = 'patent'
    key_p: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    app_date: Mapped[date] = mapped_column(Date)
    public_date: Mapped[date] = mapped_column(Date)
    key_c: Mapped[int] = mapped_column(ForeignKey('category.key_c'))
    key_e: Mapped[int] = mapped_column(ForeignKey('entity.key_e'))

    category = relationship("Categories")
    entity = relationship("Entities")

class Entities(Base):
    __tablename__ = 'entity'
    key_e: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    entity_type: Mapped[str] = mapped_column(String(50), nullable=False)
    INN: Mapped[str] = mapped_column(String(12))
    OGRN: Mapped[str] = mapped_column(String(13))
    OGRNIP: Mapped[str] = mapped_column(String(15))
    person_id: Mapped[str] = mapped_column(String(20))

class PatentOwners(Base):
    __tablename__ = 'patent_owner'
    key_po: Mapped[int] = mapped_column(primary_key=True)
    key_p: Mapped[int] = mapped_column(ForeignKey('patent.key_p'))
    key_e: Mapped[int] = mapped_column(ForeignKey('entity.key_e'))

    patent = relationship("Patents")
    entity = relationship("Entities")

class Categories(Base): 
    __tablename__ = 'category'
    key_c: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(255), nullable=False)

class PatentStats(Base):
    __tablename__ = 'patent_stat'
    key_s: Mapped[int] = mapped_column(primary_key=True)
    key_p: Mapped[int] = mapped_column(ForeignKey('patent.key_p'))
    total_patents: Mapped[int]
    total_owners: Mapped[int]
    owner_type_count: Mapped[dict[str, Any]] = mapped_column(JSONB)

    patent = relationship('Patents')

class DashboardData(Base):
    __tablename__ = 'dashboard_data'
    key_dash: Mapped[int] = mapped_column(primary_key=True)
    total_patents: Mapped[int]
    total_owners: Mapped[int]
    category_stat: Mapped[dict[str, Any]]= mapped_column(JSONB)
    region_stat: Mapped[dict[str, Any]] = mapped_column(JSONB)
