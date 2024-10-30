from DataBase.models import Child
from DataBase import get_db


# Функция для добавления детей
def add_child_db(name, iin, group, birthday, parents, phone_number, status):
    with next(get_db()) as db:
        new_child = Child(name=name, iin=iin, group=group, birthday=birthday, parents=parents,
                          phone_number=phone_number, status=status)
    db.add(new_child)
    db.commit()


def get_all_child_db():
    with next(get_db()) as db:
        all_child = db.query(Child).all()
        return all_child


def get_exact_child_db(child_id):
    with next(get_db()) as db:
        exact_child = db.query(Child).filter_by(Child_id=child_id).all()
        if exact_child:
            return exact_child
        return False

# Функция для удаления
def delete_child_db(child_id):
    with next(get_db()) as db:
        delete_child = db.query(Child).filter(Child.id == child_id).first()
        if delete_child:
            return delete_child

        db.delete(delete_child_db())
        db.commit()
        return False


def update_child_db(child_id, change_info, new_info):
    with next(get_db()) as db:
        exact_child = db.query(Child).filter(Child.id == child_id).first()
        if exact_child:
            if change_info == "name":
                exact_child.name = new_info
            elif change_info == "iin":
                exact_child.iin = new_info
            elif change_info == "group":
                exact_child.group = new_info
            elif change_info == "birthday":
                exact_child.birthday = new_info
            elif change_info == "parrents":
                exact_child.parrents = new_info
            elif change_info == "phone_number":
                exact_child.phone_number = new_info
            elif change_info == "status":
                exact_child.status = new_info
            db.commit()
            return True
