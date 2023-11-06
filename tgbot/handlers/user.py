from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from tgbot.config import load_config

from tgbot.filters.admin import AdminFilter

user_router = Router()

config = load_config()


@user_router.message(F.text.contains('видел'))
@user_router.message(F.text.contains('Видел'))
async def user_start(message: Message):
    if message.from_user.id == config.misc.raf_id:
        await message.reply(f'Всем похуй, иди на хуй, @{message.from_user.username}!')


@user_router.message(F.text.lower() == 'видел')
async def user_start(message: Message):
    if not message.from_user.id in config.tg_bot.admin_ids:
        await message.reply(f'Всем похуй, иди на хуй, @{message.from_user.username}!')
