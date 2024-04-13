from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

register_buttons = [
    [InlineKeyboardButton(text="Register", callback_data="reg")]
]

register_keyboard = InlineKeyboardMarkup(
    inline_keyboard=register_buttons
)