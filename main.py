import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message()
async def handle_message(message: Message):
    user = message.from_user.username or message.from_user.full_name
    text = message.text
    await bot.send_message(ADMIN_ID, f"<b>Сообщение от @{user}:</b>\n{text}")
    await message.answer("Спасибо! Ваше сообщение передано администратору.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
        print("Старт main.py...")
        asyncio.run(main())



