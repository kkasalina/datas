import json
import telebot
import requests as req
from requests import get
from telegram import Update
from telegram.ext import Updater, CallbackContext, TypeHandler


# token_accu = 'bBAyvYwB3CDpDAI5oKa5P18UffLdALhy'
token = '6163911380:AAGsQC0y-GpDEpGXeEe4YKzldCIVk-TUy74'
bot = telebot.TeleBot(token)
num = int(input())
source = get(f"https://http.cat/{num}")
cats_memes = dict()

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

def send__cat():
    url = f'https://http.cat/{num}'
    bot.send_photo(chat_id=chat_id, photo='https://http.cat/{num}')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "👋 Привет, я бот-ошибка-кот.\n Введи, пожалуйста, код ошибки", reply_markup=markup)

# class Cat:


#     def code_errors(self, latitude: str, longitude: str, token_accu: str):
#         url_errors_key = f'https://http.cat/{num}'
#         resp_loc = req.get(url_errors_key, headers={"APIKey": token_accu})
#         json_data = json.loads(resp_loc.text)
#         code = json_data['Key']
#         return code

#     def error(self, cod_loc: str, token_accu: str):
#         url_error = f'http://dataservice.accuerror.com/forecasts/v1/hourly/12hour/{cod_loc}?apikey={token_accu}&language=ru&metric=True'
#         response = req.get(url_error, headers={"APIKey": token_accu})
#         json_data = json.loads(response.text)
#         dict_error = dict()
#         dict_error['link'] = json_data[0]['MobileLink']
#         dict_error['сейчас'] = {
#             'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
#         for i in range(len(json_data)):
#             time = 'через' + str(i) + 'ч'
#             dict_error[time] = {
#                 'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
#         return dict_error

#     def print_cats(self, dict_error, message):
#         bot.send_message(message.chat.id, f'Докладываю (*・ω・)ﾉ\n'
#                          f'Температура сейчас {dict_error["сейчас"]["temp"]}!\n'
#                          f'А на небе {dict_error["сейчас"]["sky"]} ∠( ᐛ 」∠)＿\n'
#                          f'Температура через три часа {dict_error["через3ч"]["temp"]}!\n'
#                          f'А на небе {dict_error["через3ч"]["sky"]} (´｡• ᵕ •｡`) ♡\n'
#                          f'Температура через шесть часов {dict_error["через6ч"]["temp"]}!\n'
#                          f'А на небе {dict_error["через6ч"]["sky"]} (ﾉ´ヮ`)ﾉ*: ･ﾟ\n'
#                          f'Температура через девять часов {dict_error["через9ч"]["temp"]}!\n'
#                          f'А на небе {dict_error["через9ч"]["sky"]} (╯✧▽✧)╯')
#         bot.send_message(message.chat.id, f'А здесь ссылка на подробности ( o˘◡˘o)'
#                          f'{dict_error["link"]}')

    # def big_weather(self, message, city):
    #     latitude, longitude = self.geo_pos(city)
    #     cod_loc = self.code_errors(latitude, longitude, token_accu)
    #     you_weather = self.weather(cod_loc, token_accu)
    #     self.print_weather(you_weather, message)

    # def add_city(self, message):
    #     try:
    #         latitude, longitude = self.geo_pos(
    #             message.text.lower().split('город ')[1])
    #         cats_memes[message.from_user.id] = message.text.split('город ')[1]
    #         with open('cats_memes.json', 'w') as f:
    #             f.write(json.dumps(cats_memes))
    #         return cats_memes, 0
    #     except Exception as err:
    #         return cats_memes, 1


# C = Cat()


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.from_user.id, "👋 Привет, я бот-ошибка-кот.\n Введи, пожалуйста, код ошибки", reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     global cats_memes
#     if message.text.lower() == 'привет' or message.text.lower() == 'привет!':
#         bot.send_message(message.from_user.id,
#                          f'{message.from_user.first_name}!'
#                          f' Напиши  слово "погода", и я напишу погоду в городе,'
#                          f' где ты проживаешь или напиши название города в котором ты сейчас находишься (ღ˘⌣˘ღ)')
#     elif message.text.lower() == 'погода':
#         if message.from_user.id in cats_memes.keys():
#             city = cats_memes[message.from_user.id]
#             bot.send_message(message.from_user.id, f'О, милашка {message.from_user.first_name}!'
#                                                    f' Твой город {city}★')

#             C.big_weather(message, city)

#         else:
#             bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
#                                                    f' Я не знаю твой город ( ‾́ ◡ ‾́ )! Просто напиши:'
#                                                    f'"Мой город *****" и я запомню его!')
#     elif message.text.lower()[:9] == 'мой город':
#         cats_memes, flag = C.add_city(message)
#         if flag == 0:
#             bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
#                                                    f' Теперь я знаю твой город ヽ(>∀<☆)ノ! Это'
#                                                    f' {cats_memes[message.from_user.id]}')
#         else:
#             bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
#                                                    f' Что то пошло не так (ಥ﹏ಥ)')


def main() -> None:
    updater = Updater("6163911380:AAGsQC0y-GpDEpGXeEe4YKzldCIVk-TUy74")

    updater.dispatcher.add_handler(TypeHandler(Update, echo))

    updater.start_polling()

    print('Started')

    updater.idle()


if __name__ == "__main__":
    main()
