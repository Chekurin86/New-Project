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
users = {}

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
    # Если пользователь только запустил бота и его нет в словаре
    #users - добавляем его в словарь
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            "in_game": False,
            "secret_number": None,
            "attempts": None,
            "total_games": 0,
            "wins": 0
        }

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
        f"Всего игр сыграно: {users[message.from_user.id]['total_games']}\n"
        f"Игр выиграно: {users[message.from_user.id]['wins']}"
    )

# Этот хендлер будет срабатывать на команду "/cancel"
@dp.message(Command(commands="cancel"))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]["in_game"]:
        users[message.from_user.id]["in_game"] = False
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
    if not users[message.from_user.id]["in_game"]:
        users[message.from_user.id]["in_game"] = True
        users[message.from_user.id]["secret_number"] = get_random_number()
        users[message.from_user.id]["attempts"] = ATTEMPTS
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
    if not users[message.from_user.id]["in_game"]:
        await message.answer(
            "Жаль :(\n\nЕсли захотите поиграть - просто "
            "напишите мне об этом"
        )
    else:
        await message.answer(
            "Мы же сейчас с вами играем. Присылайте, "
            "пожалуйста, числа от 1 до 100"
        )

# Этот хендлер будет срабатывать на отправку пользователем числа от 1 до 100
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if users[message.from_user.id]["in_game"]:
        if int(message.text) == users[message.from_user.id]["secret_number"]:
            users[message.from_user.id]["in_game"] = False
            users[message.from_user.id]["total_games"] += 1
            users[message.from_user.id]["wins"] += 1
            await message.answer(
                "Ура!!! Вы угадали число!\n\n"
                "Может, сыграем еще раз?"
            )
        elif int(message.text) > users[message.from_user.id]["secret_number"]:
            users[message.from_user.id]["attempts"] -= 1
            await message.answer("Мое число меньше")
        elif int(message.text) < users[message.from_user.id]["secret_number"]:
            users[message.from_user.id]["attempts"] -= 1
            await message.answer("Мое число больше")

        if users[message.from_user.id]["attempts"] == 0:
            users[message.from_user.id]["in_game"] = False
            users[message.from_user.id]["total_games"] += 1
            await  message.answer(
                f"К сожалению, у вас больше не осталось "
                f"попыток. Вы проиграли :(\n\nМое число "
                f" было {users[message.from_user.id]['secret_number']}\n\nДавайте "
                f"сыграем еще раз?"
            )
    else:
        await message.answer("Мы еще не играем. Хотите сыграть?")

# Этот хендлер будет срабатывать на все остальные сообщения
@dp.message()
async def process_other_answers(message: Message):
    if users[message.from_user.id]["in_game"]:
        await message.answer(
            "Мы же с вами играем. "
            "Присылайте, пожалуйста, числа от 1 до 100"
        )
    else:
        await message.answer(
            "Я довольно ограниченный бот, давайте "
            "просто сыграем в игру?"
        )

if __name__ == "__main__":
    dp.run_polling(bot)
