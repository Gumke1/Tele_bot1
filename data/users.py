import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tg_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    where_from = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    where_to = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone_user = sqlalchemy.Column(sqlalchemy.String, nullable=True)

