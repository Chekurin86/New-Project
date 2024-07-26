from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Router

router = Router()

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
btn_1 = KeyboardButton(text="Камень")
btn_2 = KeyboardButton(text="Ножницы")
btn_3 = KeyboardButton(text="Бумага")

# Создаем объект клавиатуры
placeholder_kb = ReplyKeyboardMarkup(
    keyboard=[[btn_1], [btn_2], [btn_3]],
    resize_keyboard=True,
    input_field_placeholder="Выберите кнопку: камень, ножницы или бумагу"
)






