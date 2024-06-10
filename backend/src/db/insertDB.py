
import pandas as pd
from models import *
from src.database import async_session_factory


async def insert_data_from_csv(filename):
    df = pd.read_csv(filename)
    
    async with async_session_factory() as session:
        for index, row in df.iterrows():

            entity = Entities(
                name=row['Наименование полное'],
                entityType='Головная компания' if row['Головная компания (1) или филиал (0)'] == 1 else 'Филиал',
                INN=row['ИНН'],
                OGRN=row['ОГРН'],
                PersonID=row.get('ФИО директора', None)
            )
            session.add(entity)
            
            patent = Patents(
                Title=row['Title'],
                Description=row['Description'],
                AppDate=row['AppDate'],
                publicDate=row['publicDate'],
                keyC=row['keyC'],
                keyE=row['keyE']
            )
            session.add(patent)
            
            owner = PatentOwners(
                keyP=row['keyP'],
                keyE=row['keyE']
            )
            session.add(owner)
            
            category = Categories(
                Category=row['Category']
            )
            session.add(category)
            
            patent_stat = PatentStat(
                keyP=row['keyP'],
                TotalPatents=row['TotalPatents'],
                TotalOwners=row['TotalOwners'],
                OwnerTypeCount=row['OwnerTypeCount']
            )
            session.add(patent_stat)
            
            data = DashbData(
                TotalPatents=row['TotalPatents'],
                TotalOwners=row['TotalOwners'],
                CategoryStat=row['CategoryStat'],
                RegionStat=row['RegionStat']
            )
            session.add(data)

    await session.commit()
