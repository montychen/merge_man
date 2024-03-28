import os

from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse

cur_dir = os.getcwd()   # 获取当前目录

app = FastAPI()
# 假设你的 static 目录在项目根目录下
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    # return {"Hello": "World"}
    return FileResponse(f"{cur_dir}/static/index.html", media_type="text/html")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
