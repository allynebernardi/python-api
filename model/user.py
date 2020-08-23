from sqlalchemy import Column, Integer, String


class User(db.User):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    email = Column('email', String(50))


def __init__(self, name, email):
    self.name = name
    self.email = email
