from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

mood_buttons = [
    [
        InlineKeyboardButton(text="Good👍", callback_data="good"),
        InlineKeyboardButton(text="Bad👎🏿", callback_data="bad")
    ]
]

mood_keyboard = InlineKeyboardMarkup(
    inline_keyboard=mood_buttons
)
