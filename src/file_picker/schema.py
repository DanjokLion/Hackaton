from pydantic import BaseModel


class DatasetItem(BaseModel):
    name: str
    type: str
    file_id: str
