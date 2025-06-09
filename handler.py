
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

rt = Router()

@rt.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello, world!!")

@rt.message(Command('help'))
async def help(message: Message):
    await message.answer("это help")

@rt.message(F.text=='Как дела?')
async def how_are_you(message: Message):
    await message.answer("OK!")