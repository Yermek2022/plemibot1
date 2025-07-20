import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я Пленный Бот 11. Готов к работе.")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("✅ Бот запускается...")
    await dp.start_polling(bot)

if _name_ == "_main_":
    asyncio.run(main())
