from DataBase.models import Groups
from DataBase import get_db

# Функция для добавления группы
def add_groups_db(old, groups_name, user_id, quantity=0, type=None, lang=None):
    with next(get_db()) as db:
        if lang in ["Русский", "English", "Узб", "Казах"]:
            new_groups = Groups(old=old, groups_name=groups_name, user_id=user_id, quantity=quantity,
                               type=type, lang=lang)
            db.add(new_groups)
            db.commit()
            return True
        return False

# Функция для получения всех групп
def get_all_groups_db():
    with next(get_db()) as db:
        all_groups = db.query(Groups).all()
        return all_groups

# Функция для получения определённой группы
def get_exact_groups_db(groups_id):
    with next(get_db()) as db:
        exact_group = db.query(Groups).filter_by(id=groups_id).first()
        if exact_group:
            return exact_group
        return False

# Функция для удаления
def delete_groups_db(groups_id):
    with next(get_db()) as db:
        delete_groups = db.query(Groups).filter(Groups.id == groups_id).first()
        if delete_groups:
            return delete_groups

        db.delete(delete_groups_db())
        db.commit()
        return False

# Функция для изменения
def update_groups_db(groups_id, change_info, new_info):
    with next(get_db()) as db:
        exact_group = db.query(Groups).filter(Groups.id == groups_id).first()
        if exact_group:
            if change_info == "old":
                exact_group.old = new_info
            elif change_info == "group_name":
                exact_group.group_name = new_info
            elif change_info == "user_id":
                exact_group.user.id = new_info
            elif change_info == "quantity":
                exact_group.quantity = new_info
            elif change_info == "type":
                exact_group.type = new_info
            db.commit()
            return True
