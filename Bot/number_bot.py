import requests
import json
import telebot
from telebot import types


token = '6251853623:AAEX8zbgts-mZgDcNmDlxEwCocVQHzmek10'
bot = telebot.TeleBot(token)

class Bot:
    
    def buttons():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Информация про случайное число")
        btn2 = types.KeyboardButton("Информация про случайную дату")
        btn3 = types.KeyboardButton("Информация про случайный год")
        btn4 = types.KeyboardButton("Информация про случайный факт из математики")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        return markup

    
    def commands():
        @bot.message_handler(commands=['start'])
        def start(message):
            bot.send_message(message.chat.id, 'Hello! I\'m number-bot. Give me a number ', reply_markup=Bot.buttons())
            
    def answer_bot():
        @bot.message_handler(regexp='[0-9]+')
        def start(message):
            try:
                answer = requests.get(f'http://numbersapi.com/{message.text}?json')
                bot.send_message(message.chat.id, json.loads(answer.text)['text'], reply_markup=Bot.buttons())
                print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text, json.loads(answer.text)['text'])
            except:
                bot.send_message(message.chat.id, 'Что-то пошло не так😢 Пожалуйста, попробуй еще раз!', reply_markup=Bot.buttons())
                print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text)
                
    def func_message():
        @bot.message_handler(content_types=['text'])
        def func(message):
            if (message.text == "Информация про случайное число"):
                text = "random/trivia"
                answer = requests.get(f'http://numbersapi.com/{text}?json')
                bot.send_message(message.chat.id, json.loads(answer.text)['text'], reply_markup=Bot.buttons())
            elif (message.text == "Информация про случайную дату"):
                text = "random/date"
                answer = requests.get(f'http://numbersapi.com/{text}?json')
                bot.send_message(message.chat.id, json.loads(answer.text)['text'], reply_markup=Bot.buttons())
            elif (message.text == "Информация про случайный год"):
                text = "random/year"
                answer = requests.get(f'http://numbersapi.com/{text}?json')
                bot.send_message(message.chat.id, json.loads(answer.text)['text'], reply_markup=Bot.buttons())
            elif (message.text == "Информация про случайный факт из математики"):
                text = "random/math"
                answer = requests.get(f'http://numbersapi.com/{text}?json')
                bot.send_message(message.chat.id, json.loads(answer.text)['text'], reply_markup=Bot.buttons())
            else:
                bot.send_message(message.chat.id, 'Ups😢 Please, try again!', reply_markup=Bot.buttons())
                print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text)


Bot.buttons()
Bot.commands()
Bot.answer_bot()
Bot.func_message()


bot.polling()