from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.repository import UserRepository

class CheckUserFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if UserRepository.get_user(message.from_user.id):
            return False
        return True