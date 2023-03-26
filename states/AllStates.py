from aiogram.dispatcher.filters.state import StatesGroup, State


class Files_state(StatesGroup):
    get_photo = State()
    photo_title = State()
    get_audio = State()
    audio_title = State()
