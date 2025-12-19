
import asyncio

from aiogram import Dispatcher, filters
from aiogram.types import Message
from aiogram import Bot


dp = Dispatcher()


@dp.message(filters.CommandStart())
async def start(message: Message):
    print(message)



async def main():
    bot = Bot(token="8208114695:AAGc4uZwaIfgvHWNz1pFVPbZ_AnSv9WO0Kc")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
