import telebot
import datetime
from pprint import pprint
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = telebot.TeleBot('5947033600:AAF6rJihphkXcxkzAVQVYwZXkV8mUM1XDUY')
token_open_weather = ('8fff1770420e67a485593b01210eda78')
dp = Dispatcher(bot)

@dp.message_handlers(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! напишиназвание города")

@dp.message_handlers ()
async def get_weather(message: types.Message):
def get_weather(city, token_open_weather):
    try:
        z = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_open_weather }&units=metric")

        data = z.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}C°\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"Хорошего дня)"
              )

    except:
        await message.reply("Проверьте название города")

if __name__ == '__main__':
    executor.start_polling(dp)



