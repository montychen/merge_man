import os

from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse

from pydantic import BaseModel

class Body_Component(BaseModel):
    group1: str
    group2: str


cur_dir = os.getcwd()   # 获取当前目录

app = FastAPI()
# 假设你的 static 目录在项目根目录下
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    # return {"Hello": "World"}
    return FileResponse(f"{cur_dir}/static/index.html", media_type="text/html")

@app.get("/test", response_class=HTMLResponse)
def test():
    # return {"Hello": "World"}
    return FileResponse(f"{cur_dir}/static/test.html", media_type="text/html")

@app.post("/merge", response_class=PlainTextResponse)
def merge(body_com: Body_Component):
    print(f"\n{body_com}\n")
    return "http://127.0.0.1:8000/static/img/girl1.png"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
