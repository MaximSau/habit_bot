from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import asyncpg
import db

start_router = Router()

@start_router.message(Command("start"))
async def cmd_start(message: Message, pool: asyncpg.Pool):
    if message.from_user is None:
            return
    tg_id = message.from_user.id

    _ = await db.add_user(pool, tg_id)
    await message.answer('''
    Привет, это бот для учета привычек, тут можно отмечать выполнение добавленной привычки, список команд:

        /start - перезагрузить бота
        /add - добавить привычку
        /list - список привычек
        /done - отметить выполнение привычки
        /stats - статистика
    ''')
