from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove
from tgbot.config import load_config
from aiogram.dispatcher.filters.builtin import RegexpCommandsFilter

from tgbot.filters.admin import AdminFilter

user_router = Router()

config = load_config()


@user_router.message(Text(regexp=r'(?i)видел'))
@user_router.message(F.text.contains('Видел'))
async def user_start(message: Message):
    if message.from_user.id == config.misc.raf_id:
        await message.reply(f'Всем похуй, иди на хуй, @{message.from_user.username}!')


@user_router.message(F.text.lower() == 'видел')
@user_router.message(F.text.lower() == 'видал')
@user_router.message(F.text.lower() == 'теселем')
@user_router.message(F.text.lower() == 'тесселем')
@user_router.message(F.text.lower() == 'тессел ем')
@user_router.message(F.text.lower() == 'тесел ем')
@user_router.message(F.text.lower() == 'тес ел ем')
@user_router.message(F.text.lower() == 'тес эл ем')
@user_router.message(F.text.lower() == 'тесацрелем')
async def user_start(message: Message):
    if not message.from_user.id in config.tg_bot.admin_ids:
        await message.reply(f'Всем похуй, иди на хуй, @{message.from_user.username}!')


@user_router.message(Command('remove_reply'))
async def remove_reply(message: Message):
    await message.answer(f'Клавиатура очищена!', reply_markup=ReplyKeyboardRemove())