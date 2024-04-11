from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.reply(
        f"Hi, {message.from_user.full_name}"
    )


@router.message(F.text)
async def copy(message: Message):
    await message.answer(message.text)
