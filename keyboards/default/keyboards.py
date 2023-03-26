from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_menu_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("Rasm qoshish")
    btn.row("audio qoshish")
    btn.row("mening fayllarim")
    return btn