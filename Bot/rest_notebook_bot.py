import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6163911380:AAGsQC0y-GpDEpGXeEe4YKzldCIVk-TUy74"
MSG = "Отдыхала ли ты сегодня?"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.first_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!")

    for i in range(7):
        await asyncio.sleep(20)
        await bot.send_message(user_id, MSG.format(user_name))

if __name__ == "__main__":
    executor.start_polling(dp)