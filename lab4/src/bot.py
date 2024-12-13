import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from dotenv import load_dotenv
import os
from io import BytesIO
from OCR import image_to_string
import photo_processing
import db



# bot object
load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
# dispatcher
dp = Dispatcher()


# handler for the /start command
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = "Hello! This is the basic OCR bot"
    await message.answer(welcome_text)


# handler for photos
@dp.message(F.photo)
async def handle_photo(message: types.Message, bot: Bot):
    img_stream = BytesIO()
    await bot.download(message.photo[-1], destination=img_stream)
    await message.reply(photo_processing.process_image(img_stream, message))


# Launching polling
async def main():
    await db.db_start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
