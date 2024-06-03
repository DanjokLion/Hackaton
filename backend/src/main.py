from fastapi import FastAPI
from src.file_picker.router import router as file_piker
from src.config import setting


app = FastAPI(root_path=setting.ROOT_PATH)

app.include_router(file_piker)