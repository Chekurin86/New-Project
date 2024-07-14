from random import randint
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

BOT_TOKEN: str = "7347541686:AAER4jOnrHGDZYCKwhplv62zb5IPU-25YFI"

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# Количество попыток которые даются игроку
ATTEMPTS = 5

# Словарьб в котором будут храниться данные пользователя
user = {"in_game": False,
        "secret_number": None,
        "attempts": None,
        "total_games": 0,
        "wins": 0}

# Функция, которая возвращает случайное целое число от 1 до 100
def get_random_number() -> int:
    return randint(1, 100)

# Этот хендлер будет срабатывать на команду "/start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        "Привет!\nДавайте сыграем в игру 'Угадай число'?\n\n"
        "Чтобы получить правила игры и список доступных "
        "команд - отправьте команду /help"
    )

# Этот хендлер будет срабатывать на команду "/help"
@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
        f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
        f'попыток\n\nДоступные команды:\n/help - правила '
        f'игры и список команд\n/cancel - выйти из игры\n'
        f'/stat - посмотреть статистику\n\nДавай сыграем?')

# Этот хендлер будет срабатывать на команду "/stat"
@dp.message(Command(commands="stat"))
async def process_stat_command(message: Message):
    await message.answer(
        f"Всего игр сыграно: {user['total_games']}\n"
        f"Игр выиграно: {user['wins']}"
    )

# Этот хендлер будет срабатывать на команду "/cancel"
@dp.message(Command(commands="cancel"))
async def process_cancel_command(message: Message):
    if user["in_game"]:
        user["in_game"] = False
        await message.answer("Вы вышли из игры. Если захотите сыграть "
                             "снова - напишите мне об этом")
    else:
        await message.answer(
            "А мы и так с вами сейчас не играем. "
            "Может сыграем разок?"
        )

# Этот хендлер будет срабатывать на согласие пользователя сыграть в игру
@dp.message(F.text.lower().in_(["да", "давай", "сыграем", "игра",
                                "играть", "хочу играть"]))
async def process_positive_answer(message: Message):
    if not user["in_game"]:
        user["in_game"] = True
        user["secret_number"] = get_random_number()
        user["attempts"] = ATTEMPTS
        await message.answer(
            "Ура!\n\nЯ загадал число от 1 до 100, "
            "попробуй угадать!"
        )
    else:
        await message.answer(
            "Поак мы играем в игру я могу "
            "реагировать только на числа от 1 до 100 "
            "и команды /cancel и /stat"
        )

# Этот хендлер будет срабатывать на отказ пользвателя сыграть в игру
@dp.message(F.text.lower().in_(["нет", "не", "не хочу", "не буду"]))
async def process_negative_answer(message: Message):
    if not user["in_game"]:
        await message.answer(
            "Жаль :(\n\nЕсли захотите поиграть - просто "
            "напишите мне об этом"
        )
    else:
        await message.answer(
            "Мы же сейчас с вами играем. Присылайте, "
            "пожалуйста, числа от 1 до 100"
        )





























