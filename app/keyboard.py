from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Поиск'), KeyboardButton(text='Поддержка')]],
    resize_keyboard =True,
    input_field_placeholder='Выберить пункт меню'
)
catalog_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Акции')],
    [KeyboardButton(text='Список')]],
    resize_keyboard =True
)