from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON

# ---------- Создаем клавиатуру через ReplyKeyboardBuilder-------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON["yes_button"])
button_no = KeyboardButton(text=LEXICON["no_button"])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай" и "Не хочу"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры

# Создаем кнопки
button_1 = KeyboardButton(text=LEXICON['rock'])
button_2 = KeyboardButton(text=LEXICON['scissors'])
button_3 = KeyboardButton(text=LEXICON['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True
)






