from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.testing.suite.test_reflection import users
from sqlalchemy.orm import relationship

from DataBase import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    iin = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    position = Column(String, default="Воспитатель")
    status = Column(String, default="Трудоустроен")
    group = Column(Integer, ForeignKey("groups.id"))

    group_fk = relationship("Groups", back_populates="user_fk")

class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    iin = Column(String, nullable=False)
    group = Column(Integer, ForeignKey("groups.id"))
    birthday = Column(String, nullable=False)
    parents = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    status = Column(String, default="Зачислен")

    group_fk = relationship("Groups", back_populates="child_fk")

class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, autoincrement=True, primary_key=True)
    old = Column(Integer, nullable=False)
    group_name = Column(String, nullable=False)
    lang = Column(String, default="Русский")
    quantity = Column(Integer, default=0)
    type = Column(String, default="Общеобразовательная")
    user_id = Column(Integer, ForeignKey("users.id"))

    user_fk = relationship("User", lazy="subquery", back_populates="group_fk")
    child_fk = relationship("Child", lazy="subquery", back_populates="group_fk")
