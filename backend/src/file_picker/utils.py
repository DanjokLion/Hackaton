from fastapi import File, UploadFile
from src.database import async_session_factory
import aiofiles
from src.file_picker.schema import DatasetItem
from typing import Tuple
from src.config import setting
from src.db_model.model import Datasets

async def save_upload_file(upload_file, path) -> None:
    async with aiofiles.open(path, 'wb') as out_file:
        while content := await upload_file.read(1024*1024):  # читаем файл порциями по мегабайту
            await out_file.write(content)

async def generate_new_properties(file: DatasetItem) -> Tuple[DatasetItem, str]:
    item.file_id = uuid4().hex + os.path.splitext(item.name)[1]
    path = os.path.join(DATASET_DIR, item.file_id)
    return item, path

async def add_dataset_to_db(item: DatasetItem) -> None:
    async with async_session_factory() as session:   
        record = Datasets(
            name=item.name, 
            type=item.type, 
            path=os.path.join(DATASET_DIR, item.file_id)
        )
        session.add(record)
        await session.commit()
    