import os

from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static") # 假设你的 static 目录在项目根目录下

templates = Jinja2Templates(directory="static")    # 声明 模板文件放在 static 目录下



class Body_Component(BaseModel):   # 接收客户端 Post请求发过来的参数
    hair: str
    head: str
    expression: str

    body: str
    
    lhand: str    # 左手
    rhand: str    # 右手
    lfoot: str    # 左腿
    rfoot: str    # 右腿


def fill_body_com_list() -> list:
    # 收集：身体部件的目录名  和 它下面的png文件。   ["头",[这里会包含这个目录下所有的png文件名]] 
    # [['头', "head", ['27_head.png', '19_head.png', 'head.png', '31_head.png', '30_head.png']]]
    body_com_list = [["发型", "hair", []], ["头", "head", []],  ["表情", "expression", []],  ["身体", "body", []],  
                     ["左手", "lhand", []], ["右手", "rhand", []],  ["左腿", "lfoot", []],  ["右腿", "rfoot", []]  ]  
    cur_dir = os.getcwd()   # 获取当前目录
    for item in body_com_list:
        file_dir = os.path.join(cur_dir, "static/body_com", item[0])
        # print(file_dir)
        for filename in os.listdir(file_dir):
            if filename.lower().endswith(".png"):
                item[2].append(filename)
        # print( len(item[1]), "\n", item[1])
    return body_com_list

def get_body_com_url_pre() -> str:  # "http://127.0.0.1:8000/static/body_com/头/19_head.png"
    return "static/body_com"


@app.get("/", response_class=HTMLResponse)  # response_class=HTMLResponse 指明响应是一个 HTML
async def home_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"body_com_list": fill_body_com_list(), "body_com_url_pre": get_body_com_url_pre()}
    )

@app.post("/merge", response_class=PlainTextResponse)
def merge(body_com: Body_Component):
    print(f"\n{body_com}\n")
    return "http://127.0.0.1:8000/static/img/girl1.png"



@app.get("/test", response_class=HTMLResponse)
def test():
    cur_dir = os.getcwd()   # 获取当前目录
    return FileResponse(f"{cur_dir}/static/test.html", media_type="text/html")



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
