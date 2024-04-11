from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

dishes_buttons = [
    [KeyboardButton(text="Pure")],
    [KeyboardButton(text="Cotlete")]
]

dishes_keyboard = ReplyKeyboardMarkup(
    keyboard=dishes_buttons,
    resize_keyboard=True
)