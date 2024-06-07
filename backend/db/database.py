from sqlalchemy import create_engine, Column, integer, String, Text, Date, ForeignKey, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('')
Base = declarative_base()

class Patent(Base):
    __tablename__ = 'patents'

    keyP = Column(integer, primary_key=True)
    Title = Column(String(255), nullable=False)
    Description = Column(Text)
    AppDate = Column(Date)
    publicDate = Column(Date)
    keyC = Column(integer, ForeignKey('categories.keyC'))
    keyE = Column(integer, ForeignKey('entities.keyE'))

    category = relationship("Category")
    entity = relationship("Entity")

class Entities(Base):
    __tablename__ = 'entities'

    keyE = Column(integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    entityType = Column(String(50), nullable=False)
    INN = Column(String(12))
    OGRN = Column(String(13))
    OGRNIP = Column(String(15))
    personID = Column(String(20))

class PatentOwners(Base):
    __tablename__ = 'patent_owners'

    keyPO = Column(integer, primary_key=True)
    keyP = Column(integer, ForeignKey('patents.keyP'))
    keyE = Column(integer, ForeignKey('entities.keyE'))

    patent = relationship("Patent")
    entity = relationship("Entity")

class Categories(Base):
    __tablename__ = 'categories'

    keyC = Column(integer, primary_key=True)
    Category = Column(String(255), nullable=False)

class PatentStat(Base):
    __tablename__ = 'patent_stat'

    KeyS= Column(integer, primary_key=True)
    keyP = Column(integer, ForeignKey('patents.keyP'))
    TotalPatents = Column(integer)
    TotalOwners = Column(integer)
    OwnerTypeCount = Column(JSONB)

    patent = relationship('Patent')


class DashboardData(Base):
    __tablename__ = 'dashboard_data'

    keyDASH = Column(integer, primary_key=True)
    TotalPatents = Column(integer)
    TotalOwners = Column(integer)
    CategoryStat = Column(JSONB)
    RegionStat = Column(JSONB)

Base.metadates.create_all(engine)


