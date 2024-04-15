from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.inline_keyboards.register_keyboard import register_keyboard
from keyboards.inline_keyboards.sex_keyboard import sex_keyboard
from keyboards.reply_keyboards.main_keyboard import main_keyboard
from database.repository import UserRepository
from filters.check_user_filter import CheckUserFilter


router = Router()


class Registration(StatesGroup):
    name_input = State()
    sex_input = State()


@router.message(Command("start"), CheckUserFilter())
async def start(message: Message):
    await message.reply(
        f"Hi, {message.from_user.full_name}",
        reply_markup=register_keyboard
    )


@router.callback_query(F.data == "reg")
async def start(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Input your name:")
    await state.set_state(Registration.name_input)
    await callback.answer()


@router.message(Registration.name_input, F.text)
async def input_registration_name(message: Message, state: FSMContext):
    await message.answer(
        f"Your name is: {message.text}\n"
        "Now input your sex (either male or female)",
        reply_markup=sex_keyboard
    )
    await state.update_data({message.from_user.id: message.text})
    await state.set_state(Registration.sex_input)


@router.message(Registration.name_input)
async def error_mesage(message: Message):
    await message.answer(
        f"Xuinia twoi message!"
    )


@router.callback_query(Registration.sex_input, F.data.startswith("sex_"))
async def input_registration_sex(callback: CallbackQuery, state: FSMContext):
    sex = callback.data.split("_")[-1]
    data = await state.get_data()
    UserRepository.create(
        telegram_id=callback.from_user.id,
        name=data[callback.from_user.id],
        sex=sex
    )
    await callback.message.edit_text(
        f"Your sex is: {sex}\n"
    )
    await callback.message.answer(
        "Your account has been created",
        reply_markup=main_keyboard
    )
    
    await state.clear()
    
