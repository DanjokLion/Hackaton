from fastapi import FastAPI

from src.config import setting


app = FastAPI(root_path=setting.ROOT_PATH)

@app.get("/")
def read_root():
    return {"Hello": "World"}