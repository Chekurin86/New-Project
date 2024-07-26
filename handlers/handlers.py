from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Инициализируем ротер уровня модуля
router = Router()

kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
btn_1 = KeyboardButton(text="Камень")
btn_2 = KeyboardButton(text="Ножницы")
btn_3 = KeyboardButton(text="Бумага")

kb_builder.row(btn_1, width=1)
kb_builder.row(btn_2, width=1)
kb_builder.row(btn_3, width=1)


# Этот хендлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON["/start"],
        reply_markup=kb_builder.as_markup(resize_keyboard=True),
        input_field_placeholder="Выберите кнопку: камень, ножницы или бумагу"
    )

# Этот хендлер срабатывает на команду /help
@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON["/help"])