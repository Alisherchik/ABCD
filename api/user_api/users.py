from fastapi import APIRouter
from DataBase.userservice import add_user_db, get_exact_user_db, get_all_users_db, update_user_db, delete_user_db
from pydantic import BaseModel
from typing import Optional
import re


user_router = APIRouter(prefix="/user", tags=["Пользователи"])

regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")

def check_name(name):
    if re.fullmatch(regex, name):
        return True
    return False

class User(BaseModel):
    login: str
    password: str
    name: str
    iin: int
    phone_number: str
    position: Optional[str] = None
    status: Optional[str] = None
    group: Optional[int] = None

@user_router.post("/register_user")
async def add_user_api(user_data: User, check_login=None):
    user_db = dict(user_data)
    login_validation = check_login(user_data.login)
    if login_validation:
        result = add_user_db(**user_db)
        return {"status": 1, "message": "Пользователь успешно добавлен"}
    return {"status": 0, "message": "Неправильный логин"}

@user_router.get("/get_exact_user")
async def get_exact_user_api(user_id: int):
    result = get_exact_user_db(user_id)
    if result:
        return {"f: пользователь {user_id}"}
    return result

@user_router.get("/get_all_user")
async def get_all_users_api():
    result = get_all_users_db()
    if result:
        return "Все пользователи"
    return result

@user_router.put("/update_user_info")
async def update_user_api(user_id: int, change_info: str, new_info: str):
    result = update_user_db(user_id, change_info, new_info)
    if result:
        return "Данные успешно изменены"
    return result

@user_router.delete("/delete_user")
async def delete_user_api(user_id: int):
    result = delete_user_db(user_id)
    if result:
        return "Пользователь удалён"
    return result
