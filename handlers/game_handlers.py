from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon import LEXICON
from random import choice


VARIANTS = ("Камень", "Ножницы", "Бумага")

# Инициализируем роутер уровня модуля
router = Router()

# Этот хэндлер будет срабатывать при выбранном варианте "камень"
@router.message(F.text == "Камень")
async def stone_choice(message: Message):
    AI_choice = choice(VARIANTS)
    await message.answer(AI_choice)
    if AI_choice == "Камень":
        await message.answer(LEXICON["draw"])
    elif AI_choice == "Ножницы":
        await message.answer(LEXICON["win"])
    elif AI_choice == "Бумага":
        await message.answer(LEXICON["lose"])

# Этот хэндлер будет срабатывать при выбранном варианте "ножницы"
@router.message(F.text == "Ножницы")
async def scissors_choice(message: Message):
    AI_choice = choice(VARIANTS)
    await message.answer(AI_choice)
    if AI_choice == "Камень":
        await message.answer(LEXICON["lose"])
    elif AI_choice == "Ножницы":
        await message.answer(LEXICON["draw"])
    elif AI_choice == "Бумага":
        await message.answer(LEXICON["win"])

# Этот хэндлер будет срабатывать при выбранном варианте "бумага"
@router.message(F.text =="Бумага")
async def paper_choice(message: Message):
    AI_choice = choice(VARIANTS)
    await message.answer(AI_choice)
    if AI_choice == "Камень":
        await message.answer(LEXICON["win"])
    elif AI_choice == "Ножницы":
        await message.answer(LEXICON["lose"])
    elif AI_choice == "Бумага":
        await message.answer(LEXICON["draw"])

# Этот хэндлер будет срабатывать при выбранном варианте "бумага"
@router.message()
async def other_choice(message: Message):
    await message.answer(LEXICON["other"])

