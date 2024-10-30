from fastapi import APIRouter
from DataBase.childservice import add_child_db, get_exact_child_db, get_all_child_db, update_child_db, delete_child_db
from pydantic import BaseModel
from typing import Optional
import re


child_router = APIRouter(prefix="/child", tags=["Дети"])

regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")

def check_name(name):
    if re.fullmatch(regex, name):
        return True
    return False

class Child(BaseModel):
    name: str
    iin: int
    phone_number: str
    birthday: str
    parents: str
    status: Optional[str] = None
    group: Optional[int] = None

@child_router.post("/register_child")
async def add_child_api(child_data: Child, check_name=None):
    child_db = dict(child_data)
    name_validation = check_name(child_data.name)
    if name_validation:
        result = add_child_db(**child_db)
        return {"status": 1, "message": "Пользователь успешно добавлен"}
    return {"status": 0, "message": "Неправильное имя"}

@child_router.get("/get_exact_child")
async def get_exact_child_api(child_id: int):
    result = get_exact_child_db(child_id)
    if result:
        return "f пользователь {child_id}"
    return result

@child_router.get("/get_all_child")
async def get_all_child_api():
    result = get_all_child_db()
    if result:
        return "Все дети"
    return result

@child_router.put("/update_child_info")
async def update_child_api(child_id: int, change_info: str, new_info: str):
    result = update_child_db(child_id, change_info, new_info)
    if result:
        return "Данные успешно изменены"
    return result

@child_router.delete("/delete_child")
async def delete_child_api(child_id: int):
    result = delete_child_db(child_id)
    if result:
        return "Ребёнок удалён"
    return result
