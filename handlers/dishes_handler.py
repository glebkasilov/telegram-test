from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.dishes_keyboard import dishes_keyboard
from keyboards.main_keyboard import main_keyboard

router = Router()


@router.message(Command("dishes"))
async def dishes(message: Message):
    await message.reply(
        f"Whose your dish, {message.from_user.full_name}:",
        reply_markup=dishes_keyboard
    )


@router.message(F.text == "Pure")
async def print_Pure(message: Message):
    await message.answer(
        f"Your dish is Pure, {message.from_user.first_name}",
        reply_markup=main_keyboard
    )


@router.message(F.text == "Cotlete")
async def print_Cotlete(message: Message):
    await message.answer(
        f"Your dish is Cotlete, {message.from_user.first_name}",
        reply_markup=main_keyboard
    )