from fastapi import APIRouter
from DataBase.groupservice import add_groups_db, get_exact_groups_db, get_all_groups_db, update_groups_db, delete_groups_db
from pydantic import BaseModel
from typing import Optional
import re


groups_router = APIRouter(prefix="/groups", tags=["Группы"])

regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")

def check_name(name):
    if re.fullmatch(regex, name):
        return True
    return False

class Groups(BaseModel):
    old: int
    group_name: str
    lang: Optional[str] = None
    quantity: int
    type: str
    user_id: Optional[int] = None


@groups_router.post("/register_groups")
async def add_groups_api(groups_data: Groups, check_groups_name=None, check_old=None):
    groups_db = dict(groups_data)


    # Проверяем возраст и название группы
    old_validation = check_old(groups_data.old)
    groups_name_validation = check_groups_name(groups_data.group_name)

    # Проверяем оба условия
    if old_validation and groups_name_validation:
        # Убираем лишние скобки и передаём данные
        result = add_groups_db(**groups_db)
        return {"status": 1, "message": "Группа успешно добавлена"}


    # Более информативное сообщение об ошибке
    if not old_validation:
        return {"status": 0, "message": "Неправильный возраст"}
    return {"status": 0, "message": "Неправильное название группы"}



@groups_router.get("/get_exact_groups")
async def get_exact_groups_api(groups_id: int):
    result = get_exact_groups_db(groups_id)
    if result:
        return "f пользователь {user_id}"
    return result

@groups_router.get("/get_all_groups")
async def get_all_groups_api():
    result = get_all_groups_db()
    if result:
        return "Все пользователи"
    return result

@groups_router.put("/update_groups_info")
async def update_groups_api(groups_id: int, change_info: str, new_info: str):
    result = update_groups_db(groups_id, change_info, new_info)
    if result:
        return "Данные группы успешно изменены"
    return result

@groups_router.delete("/delete_groups")
async def delete_groups_api(groups_id: int):
    result = delete_groups_db(groups_id)
    if result:
        return "Группа удалёна"
    return result
