import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config_reader import TOKEN
from app.handlers import rt


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")

