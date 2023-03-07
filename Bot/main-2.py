import json
import telebot
import requests as req
from geopy import geocoders

token_accu = 'bBAyvYwB3CDpDAI5oKa5P18UffLdALhy'
token = '5938458549:AAFKtduATnQh16Kmc4B82wnSlcVkRXUm0Tc'
bot = telebot.TeleBot(token)
cities = dict()


class Weather:

    def geo_pos(self, city: str):
        geolocator = geocoders.Nominatim(user_agent="telebot")
        latitude = str(geolocator.geocode(city).latitude)
        longitude = str(geolocator.geocode(city).longitude)
        return latitude, longitude

    def code_location(self, latitude: str, longitude: str, token_accu: str):
        url_location_key = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={token_accu}&q={latitude},{longitude}&language=ru'
        resp_loc = req.get(url_location_key, headers={"APIKey": token_accu})
        json_data = json.loads(resp_loc.text)
        code = json_data['Key']
        return code

    def weather(self, cod_loc: str, token_accu: str):
        url_weather = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{cod_loc}?apikey={token_accu}&language=ru&metric=True'
        response = req.get(url_weather, headers={"APIKey": token_accu})
        json_data = json.loads(response.text)
        dict_weather = dict()
        dict_weather['link'] = json_data[0]['MobileLink']
        dict_weather['сейчас'] = {
            'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
        for i in range(len(json_data)):
            time = 'через' + str(i) + 'ч'
            dict_weather[time] = {
                'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
        return dict_weather

    def print_weather(self, dict_weather, message):
        bot.send_message(message.chat.id, f'Докладываю (*・ω・)ﾉ\n'
                         f'Температура сейчас {dict_weather["сейчас"]["temp"]}!\n'
                         f'А на небе {dict_weather["сейчас"]["sky"]} ∠( ᐛ 」∠)＿\n'
                         f'Температура через три часа {dict_weather["через3ч"]["temp"]}!\n'
                         f'А на небе {dict_weather["через3ч"]["sky"]} (´｡• ᵕ •｡`) ♡\n'
                         f'Температура через шесть часов {dict_weather["через6ч"]["temp"]}!\n'
                         f'А на небе {dict_weather["через6ч"]["sky"]} (ﾉ´ヮ`)ﾉ*: ･ﾟ\n'
                         f'Температура через девять часов {dict_weather["через9ч"]["temp"]}!\n'
                         f'А на небе {dict_weather["через9ч"]["sky"]} (╯✧▽✧)╯')
        bot.send_message(message.chat.id, f'А здесь ссылка на подробности ( o˘◡˘o)'
                         f'{dict_weather["link"]}')

    def big_weather(self, message, city):
        latitude, longitude = self.geo_pos(city)
        cod_loc = self.code_location(latitude, longitude, token_accu)
        you_weather = self.weather(cod_loc, token_accu)
        self.print_weather(you_weather, message)

    def add_city(self, message):
        try:
            latitude, longitude = self.geo_pos(
                message.text.lower().split('город ')[1])
            cities[message.from_user.id] = message.text.split('город ')[1]
            with open('cities.json', 'w') as f:
                f.write(json.dumps(cities))
            return cities, 0
        except Exception as err:
            return cities, 1


W = Weather()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я Тучка-бот (⌒▽⌒)☆")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global cities
    if message.text.lower() == 'привет' or message.text.lower() == 'привет!':
        bot.send_message(message.from_user.id,
                         f'{message.from_user.first_name}!'
                         f' Напиши  слово "погода", и я напишу погоду в городе,'
                         f' где ты проживаешь или напиши название города в котором ты сейчас находишься (ღ˘⌣˘ღ)')
    elif message.text.lower() == 'погода':
        if message.from_user.id in cities.keys():
            city = cities[message.from_user.id]
            bot.send_message(message.from_user.id, f'О, милашка {message.from_user.first_name}!'
                                                   f' Твой город {city}★')

            W.big_weather(message, city)

        else:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Я не знаю твой город ( ‾́ ◡ ‾́ )! Просто напиши:'
                                                   f'"Мой город *****" и я запомню его!')
    elif message.text.lower()[:9] == 'мой город':
        cities, flag = W.add_city(message)
        if flag == 0:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Теперь я знаю твой город ヽ(>∀<☆)ノ! Это'
                                                   f' {cities[message.from_user.id]}')
        else:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Что то пошло не так (ಥ﹏ಥ)')


bot.infinity_polling()
