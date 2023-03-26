from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import *

from database.connections import get_add_audio, get_all_files
from keyboards.default.keyboards import start_menu_btn
from keyboards.inline.files_btn import files_btn
from loader import dp, bot
from states.AllStates import Files_state


async def bot_start(message: Message):
    btn = await start_menu_btn()
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=btn)


async def get_audio_handler(message: Message, state: FSMContext):
    await message.answer(f"Audioni yuboring")
    await Files_state.get_audio.set()


async def get_audio(message: Message, state: FSMContext):
    audio = message.audio.file_id
    user_id = message.from_user.id
    await get_add_audio(user_id=user_id, file_id=audio)
    await message.answer(f"Audio qoshildi")
    await state.finish()


async def get_photo_handler(message: Message, state: FSMContext):
    await message.answer(f"Rasmni yuboring")
    await Files_state.get_photo.set()


async def get_photo(message: Message, state: FSMContext):
    photo = message.photo[0].file_id
    user_id = message.from_user.id
    await get_add_audio(user_id=user_id, file_id=photo)
    await message.answer("Rasm qoshildi")
    await state.finish()


async def get_files_callback(call: CallbackQuery):
    await call.answer()
    # id = call.message.from_user.id
    users = await get_all_files(call.from_user.id)
    file_id = int(call.data.split('_')[-1])

    for i in users:
        if i['id'] == file_id:
            files_id = i['file_id']
            title = i['title']
            # print(i)
            # print(files_id)
            # print(title)
            # print(f"bosildi: {i['id']}")
            # await call.message.answer(title)
            try:
                await call.message.answer_photo(files_id, caption=f"{i['id']}-{title}")
            except:
                await call.message.answer_audio(files_id, caption=f"{i['id']}-{title}")


async def all_users_handler(message: Message):
    id = message.from_user.id
    users = await get_all_files(user_id=id)
    btn = await files_btn(users)
    # print(btn)
    if users:
        await message.answer("Sizning faylaringiz", reply_markup=btn)
    else:
        await message.answer(text=f"Siz fayllar mavjud emas")

    # btn = await files_btn(user)
    # await message.answer("salom", reply_markup=btn)
    # print(user)
    # print(btn)
    # btn  = await files_btn(user_id=message.from_user.id)
    # await message.answer("malumotlar", reply_markup=btn)
    # if user:
    #     for users in user:
    #         user_id = users['user_id']
    #         file_id = users['file_id']
    #         try:
    #             await message.answer_photo(file_id, caption="Photo")
    #         except:
    #             await message.answer_audio(file_id, caption="audio")
    # else:
    #     await message.answer(text=f"Siz fayllar mavjud emas")


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(get_audio_handler, text=['audio qoshish'])
    dp.register_message_handler(get_photo_handler, text=['Rasm qoshish'])
    dp.register_message_handler(all_users_handler, text=['mening fayllarim'])

    dp.register_callback_query_handler(get_files_callback, text_contains=['file'])

    dp.register_message_handler(get_audio, state=Files_state.get_audio, content_types=['audio'])
    dp.register_message_handler(get_photo, state=Files_state.get_photo, content_types=['photo'])
