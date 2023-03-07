import requests
import json
import telebot

token = '6160079212:AAGAPLx1EGJdglmBUEYVVmAIE8rGEKtpqcw'
bot = telebot.TeleBot(token)


class Bot:
    
    def command():
        @bot.message_handler(commands=['start'])
        def start(message):
            bot.send_message(message.chat.id, '👋 Привет, я бот-ошибка-кот.\nВведи, пожалуйста, код ошибки!\nА я подберу для тебя кота🐱!')

    def answer_bot():
        @bot.message_handler(regexp='[0-9]+')
        def start(message):
            try:
                answer = requests.get(f'https://http.cat/{message.text}?json') # Обработать ответ
                bot.send_photo(message.chat.id, f'https://http.cat/{message.text}?json')     
            except:
                bot.send_message(message.chat.id, 'Что-то пошло не так😢 Пожалуйста, введи код ошибки, которую хочешь найти')



Bot.command()
Bot.answer_bot()


bot.polling()