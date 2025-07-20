from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
import asyncio
import logging
import os

# Вставь сюда свой токен Telegram-бота
TOKEN = "8157974045:AAF8DZ6PHzBDCDqCfsGSuQV_T5v2oUbkfmE"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

# Пример обработчика команды /start
@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("<b>Привет!</b> Я твой бот. Всё работает!", parse_mode=ParseMode.HTML)

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())