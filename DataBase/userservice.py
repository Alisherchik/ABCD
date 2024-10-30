from DataBase.models import User
from DataBase import get_db

# Функция для добавления пользователей
def add_user_db(login, password, name, iin, phone_number, position, status, group):
    with next(get_db()) as db:
        new_user = User(login=login, password=password, name=name, iin=iin, phone_number=phone_number,
                        position=position, status=status, group=group)
    db.add(new_user)
    db.commit()
    return True

# Функция для получения всех пользователей
def get_all_users_db():
    with next(get_db()) as db:
        all_users = db.query(User).all()
        return all_users

# Функция для получения определённого пользователя
def get_exact_user_db(user_id):
    with next(get_db()) as db:
        exact_user = db.query(User).filter_by(id=user_id).first()
        if exact_user:
            return exact_user
        return False

# Функция для удаления
def delete_user_db(user_id):
    with next(get_db()) as db:
        delete_user = db.query(User).filter(User.id == user_id).first()
        if delete_user:
            return delete_user

        db.delete(delete_user_db())
        db.commit()
        return False

# Функция для изменения
def update_user_db(user_id, login=None, password=None, name=None, iin=None, phone_number=None, position=None,
                   status=None, group=None):
    with next(get_db()) as db:
        update_user = db.query(User).filter(User.id == user_id).first()
        if not update_user:
            return False
        if login:
            update_user.login = login
        if password:
            update_user.password = password
        if name:
            update_user.name = name
        if phone_number:
            update_user.phone_number = phone_number
        if iin:
            update_user.iin = iin
        if position:
            update_user.position = position
        if status:
            update_user.status = status
        if group:
            update_user.group = group
        db.commit()
        return True
