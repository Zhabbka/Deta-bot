import datetime
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class HoroState(StatesGroup):
    horo = State()


class WeatherState(StatesGroup):
    weather = State()


bot = Bot(token='5947033600:AAF6rJihphkXcxkzAVQVYwZXkV8mUM1XDUY')
token_open_weather = '8fff1770420e67a485593b01210eda78'
dp = Dispatcher(bot, storage=MemoryStorage())

# Кнопки для клавы
horo_button = KeyboardButton('/Гороскоп')
weather_button = KeyboardButton('/Погода')
# Клава
keyboard = ReplyKeyboardMarkup()
keyboard.add(horo_button).add(weather_button)


# Регистрация команд
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(weather, commands=['Погода'])
    dp.register_message_handler(horo, commands=['Гороскоп'])


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=keyboard)


@dp.message_handler(commands=['Погода'])
async def weather(message: types.Message):
    await message.answer('Введите название города')
    await WeatherState.weather.set()


@dp.message_handler(state=WeatherState.weather)
async def weather_answer(message: types.Message, state: FSMContext):
    try:
        z = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token_open_weather}&units=metric")

        data = z.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(
            data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.answer(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                             f"Погода в городе: {city}\nТемпература: {cur_weather}C°\n"
                             f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}м/c\n"
                             f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                             f"Хорошего дня)")
        await state.finish()
    except:
        await message.reply("Проверьте название города")


@dp.message_handler(commands=['Гороскоп'])
async def horo(message: types.Message):
    await message.answer('Сейчас я расскажу тебе гороскоп на сегодня, выбери свой знак зодиака')
    keyboard = types.InlineKeyboardMarkup()
    # По очереди готовим текст и обработчик для каждого знака зодиака
    key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
    # И добавляем кнопку на экран
    keyboard.add(key_oven)
    key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
    keyboard.add(key_telec)
    key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
    keyboard.add(key_bliznecy)
    key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
    keyboard.add(key_rak)
    key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
    keyboard.add(key_lev)
    key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
    keyboard.add(key_deva)
    key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
    keyboard.add(key_vesy)
    key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
    keyboard.add(key_scorpion)
    key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
    keyboard.add(key_strelec)
    key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
    keyboard.add(key_kozerog)
    key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
    keyboard.add(key_vodoley)
    key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
    keyboard.add(key_ryby)
    # Показываем все кнопки сразу и пишем сообщение о выборе
    await bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)



@dp.message_handler(state=HoroState.horo)
async def horo_answer(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    await state.finish()




if __name__ == '__main__':
    executor.start_polling(dp)
