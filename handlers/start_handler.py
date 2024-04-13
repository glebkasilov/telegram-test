from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.inline_keyboards.register_keyboard import register_keyboard
from database.repository import UserRepository

router = Router()


class Registration(StatesGroup):
    name_input = State()
    sex_input = State()


@router.message(Command("start"))
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
        "Now input your sex (either male or female)"
    )
    await state.update_data({"name": message.text})
    await state.set_state(Registration.sex_input)


@router.message(Registration.name_input)
async def error_mesage(message: Message):
    await message.answer(
        f"Xuinia twoi message!"
    )


@router.message(Registration.sex_input, F.text)
async def input_registration_sex(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    UserRepository.create(
        telegram_id=message.from_user.id,
        name=data["name"],
        sex=message.text
    )
    await message.answer(
        f"Your sex is: {message.text}\n"
        "Your account has been created"
    )
    await state.clear()


@router.message(Registration.sex_input)
async def error_mesage(message: Message):
    await message.answer(
        f"Xuinia twoi message!"
    )
