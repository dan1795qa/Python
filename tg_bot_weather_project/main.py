import requests
from pprint import pprint
from config import open_weather_token
import datetime


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_the_day = sunset_timestamp - sunrise_timestamp

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather} C°\n"
            f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжжительность дня: {lenght_of_the_day}\n"
            f"Хорошего дня!")

    except Exception as ex:
        print(ex)
        print('Проверьте название города')

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()