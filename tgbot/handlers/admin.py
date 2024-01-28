from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.answer(f'Привет, админ, @{message.from_user.username}!')


@admin_router.message(Command('fas_raf'))
async def fas_raf(message: Message):
    await message.answer(f'Раф, соси')