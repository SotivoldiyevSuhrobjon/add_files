from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.connections import get_all_files




async def files_btn(data):
    # user = await get_all_files(user_id)
    btn = InlineKeyboardMarkup(row_width=1)
    for users in data:
        btn.add(
            InlineKeyboardButton(text=f"{users['id']} | {users['title']}", callback_data=f"file_{users['id']}" )
        )
    return btn


