from .engine import EngineController
from .models import User


class UserRepository:
    database_controller = EngineController()

    @classmethod
    def get_user(cls, user_id: int) -> User:
        session = cls.database_controller.create_session()
        user = session.query(User).filter(User.telegram_id == user_id).first()
        session.close()
        return user


    @classmethod
    def create(cls, telegram_id: str, name: str, sex: str = "other") -> None:
        session = cls.database_controller.create_session()
        user = User(
            telegram_id=telegram_id,
            name=name,
            sex=sex
        )
        session.add(user)
        session.commit()
        session.close()

    @classmethod
    def update(cls, telegram_id: str, name: str, sex: str = "other") -> User | None:
        session = cls.database_controller.create_session()
        user = session.query(User).filter(User.telegram_id == telegram_id).first()
        if user:
            user.name = name
            user.sex = sex
            session.commit()
        session.close()
        return user

    @classmethod
    def delete(cls, telegram_id: int) -> bool:
        session = cls.database_controller.create_session()
        user = session.query(User).filter(User.telegram_id == telegram_id).first()
        if user:
            session.delete(user)
            session.commit()
            session.close()
            return True

        session.close()
        return False
