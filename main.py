import asyncio
import time

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

bot = Bot(token="7413805589:AAGy3U8bylU8AOYIXOVoyrsODnhvCIw5oUI")
dp = Dispatcher()


@dp.message(Command("hello"))
async def hello(message: types.Message):
    start_time = time.time()
    await message.answer("Hello, World!")
    print(time.time() - start_time)


async def main():
    await dp.start_polling(bot) 


asyncio.run(main())
