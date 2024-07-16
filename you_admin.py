from aiogram.filters import BaseFilter
from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = "7347541686:AAER4jOnrHGDZYCKwhplv62zb5IPU-25YFI"
admin_ids: list[int] = [6991696753]

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


# Этт хендлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text="Вы админ")

# Этот хендлер будет срабатывать, если апдейт не от админа
dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text="Вы не админ")


if __name__ == "__main__":
    dp.run_polling(bot)



