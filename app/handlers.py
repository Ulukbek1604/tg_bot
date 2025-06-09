from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.keyboard as kb


rt = Router()
#Простое меню с командами: /start, /catalog, /search, /support для клиентов.
#Админ-команды: /add_product, /edit_product, /delete_product, /orders, /manage_users, /set_price, /set_discount, /analytics, /support_reply.

@rt.message(CommandStart())
async def start(message: Message):
    await message.reply(f"Привет. {message.from_user.full_name}. Это бот для покупки стим аккаунтов и ключей",
                        reply_markup=kb.main_keyboard)

@rt.message(F.text=='Каталог')
async def help(message: Message):
    await message.answer("Каталог", reply_markup=kb.catalog_keyboard)

# @rt.message(Command('search'))
# async def search(message: Message):
#     await message.answer()

# @rt.message(F.text=='')
# async def how_are_you(message: Message):
#     await message.answer("OK!")