from fastapi import FastAPI, Request
from api.group_api.groups import groups_router
from api.user_api.users import user_router
from api.child_api.childs import child_router
from DataBase import Base, engine
Base.metadata.create_all(engine)
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

abcd = FastAPI(docs_url="/")

abcd.include_router(groups_router)
abcd.include_router(user_router)
abcd.include_router(child_router)

@abcd.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(name="index.html", request=request)


asdgajs = 1232