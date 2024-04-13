from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.inline_keyboards.mood_keyboard import mood_keyboard

router = Router()


@router.message(Command("mood"))
async def how_are_you(message: Message):
    await message.answer(
        f"How are you, {message.from_user.first_name}?",
        reply_markup=mood_keyboard
    )


@router.callback_query(F.data == "good")
async def good(callback: CallbackQuery):
    await callback.message.edit_text("This is amazing!!!")
    await callback.answer()


@router.callback_query(F.data == "bad")
async def bad(callback: CallbackQuery):
    await callback.message.edit_text("I am fucking your mother)")
    await callback.answer()
