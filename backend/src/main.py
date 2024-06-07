from fastapi import FastAPI
from src.file_picker.router import router as file_piker
from src.config import setting
from fastapi.responses import FileResponse


app = FastAPI(root_path=setting.ROOT_PATH)

app.include_router(file_piker)

some_file_path = 'base.xlms'

@app.get('/')
async def upload_file():
    return FileResponse(some_file_path)
