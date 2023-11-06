from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply(f'Привет, пользователь @{message.from_user.username}!')
