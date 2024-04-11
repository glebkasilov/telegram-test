from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command

from keyboards.main_keyboard import main_keyboard

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.reply(
        f"Hi, {message.from_user.full_name}",
        reply_markup=main_keyboard
    )

@router.message(F.text == "Hi")
async def print_hi(message: Message):
    await message.answer(
        f"Hi, {message.from_user.first_name}"
    )

@router.message(F.text == "How are you?")
async def print_hi(message: Message):
    await message.answer(
        f"How are you, {message.from_user.first_name}?"
    )

@router.message(F.text == "Bye")
async def print_hi(message: Message):
    await message.answer(
        f"Bye, {message.from_user.first_name}",
        reply_markup=ReplyKeyboardRemove()
    )
