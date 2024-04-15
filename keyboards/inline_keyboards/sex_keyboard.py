from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sex_buttons = [
    [
        InlineKeyboardButton(text="Male", callback_data="sex_male"),
        InlineKeyboardButton(text="Female", callback_data="sex_female")
    ]
]

sex_keyboard = InlineKeyboardMarkup(
    inline_keyboard=sex_buttons
)
