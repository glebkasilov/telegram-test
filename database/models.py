import sqlalchemy

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    telegram_id = sqlalchemy.Column(
        sqlalchemy.String(32),
        primary_key=True,
        unique=True
    )

    name = sqlalchemy.Column(
        sqlalchemy.String(128)
    )
    
    sex = sqlalchemy.Column(
        sqlalchemy.String(5)
    )
    
    def __repr__(self) -> str:
        return f"User: {self.telegram_id}"
    