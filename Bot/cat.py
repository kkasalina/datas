import aiogram 
from aiogram import Bot, Dispatcher, executor, types
import telebot
import requests 
from requests import get

API_TOKEN = '6163911380:AAGsQC0y-GpDEpGXeEe4YKzldCIVk-TUy74'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет, я бот-ошибка-кот.\n Введи, пожалуйста, код ошибки", reply_markup=markup)



# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#    await message.reply("Привет, я бот-ошибка-кот.\n Введи, пожалуйста, код ошибки")
  
  
# num = int(input())
# source = get(f"https://http.cat/{num}")
# token = "6163911380:AAGsQC0y-GpDEpGXeEe4YKzldCIVk-TUy74"
# bot = telebot.TeleBot(token)

# @dp.message_handler()
# async def echo(message: types.Message):
#    await message.answer(source)
  
  
# if __name__ == '__main__':
#    executor.start_polling(dp, skip_updates=True)