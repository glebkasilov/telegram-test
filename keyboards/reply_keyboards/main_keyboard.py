from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_buttons = [
    [KeyboardButton(text="Hi"), KeyboardButton(text="How are you?")],
    [KeyboardButton(text="Bye")]
]

main_keyboard = ReplyKeyboardMarkup(
    keyboard=main_buttons,
    resize_keyboard=True
)
