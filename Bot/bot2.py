import requests
import json
import telebot

bot = telebot.TeleBot('6251853623:AAEX8zbgts-mZgDcNmDlxEwCocVQHzmek10')


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#      bot.reply_to(message, message.text)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(regexp='[0-9]+')
def start(message):
    answer = requests.get(f'http://numbersapi.com/{message.text}?json')
    bot.send_message(message.chat.id, json.loads(answer.text)['text'])


bot.polling()
# answer = requests.get('http://numbersapi.com/100?json')
# print(answer.status_code)
# print(answer.url)
# print((json.loads(answer.text)['']))
