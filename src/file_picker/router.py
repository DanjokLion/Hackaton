from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from src.database import get_async_session
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import DATASET_DIR
from src.file_picker.schema import DatasetItem
from src.file_picker.utils import save_upload_file
from fastapi.responses import FileResponse
import os

router = APIRouter(
    tags=["dataset"]
)

@router.post(
     "/dataset",
     summary="Загрузка файла(датасета) на обработку"
    )

async def upload_dataset(file: UploadFile, session: AsyncSession = Depends(get_async_session)):
    file_id = uuid4().hex + os.path.splitext(file.filename)[1]
    path = os.path.join(DATASET_DIR, file_id)
    item = DatasetItem(
        name = file.filename,
        type = file.content_type,
        file_id = file_id
    )
    
    # while True:
    #     query = exists(select(Dataset.path).where(Dataset.path.)).select()
    #     path_exist = (await session.execute(query)).scalar()
    #     if not path_exists:
    #         break
    #     item, path= generate_new_properties(item)
    # await add_dataset_to_db(item)

    await save_upload_file(file, path)
    
@router.get('/dataset')
async def upload_file(
    file_id:str
    ):
    return FileResponse()#pass