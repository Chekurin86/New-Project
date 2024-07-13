from aiogram import  Bot, Dispatcher, F
from  aiogram.filters import Command
from aiogram.types import  Message, ContentType

BOT_TOKEN = "7347541686:AAER4jOnrHGDZYCKwhplv62zb5IPU-25YFI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь")

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(
        "Напиши мне что-нибудь в ответ "
        " и я пришлю тебе твое сообщение"
    )


@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.answer_sticker(message.sticker.file_id)

@dp.message(F.video)
async def send_video_echo(message: Message):
    await message.answer_video(message.video.file_id)

@dp.message()
async def send_gif_echo(message: Message):
    await message.reply_animation(message.animation.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async  def send_echo(message: Message):
    if message.text is not None:
        await message.reply(text=message.text)






if __name__ == "__main__":
    dp.run_polling(bot)