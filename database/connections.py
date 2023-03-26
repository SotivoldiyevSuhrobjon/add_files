from playhouse.shortcuts import model_to_dict

from data.config import ADMINS
from .models import *


async def add_user(user_id: int, username: str):
    with db:
        if not Users.select().where(Users.user_id == user_id).exists():
            Users.create(user_id=user_id, username=username)


async def get_add_audio(user_id, file_id, ):
    with db:
        Add_files.create(user_id=user_id, file_id=file_id)


async def get_all_files(user_id: int):
    with db:
        fayl = Add_files.select().where(Add_files.user_id == user_id)
        fayllar = [model_to_dict(item) for item in fayl]
        return fayllar
