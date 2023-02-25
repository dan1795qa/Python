import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply('Привет! Напиши мне название города и я пришлю тебе сводку погоды на сегодня!')

@dp.message_handler(content_types=["text"])
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
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

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather} C°\n"
            f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжжительность дня: {lenght_of_the_day}\n"
            f"***Хорошего дня!***"
                            )

    except :
        await message.reply('\U00002620Проверьте название города\U00002620')

if __name__ == '__main__':
    executor.start_polling(dp)