import telebot
import requests

bot = telebot.TeleBot('5947033600:AAF6rJihphkXcxkzAVQVYwZXkV8mUM1XDUY')
token_open_weather = ('8fff1770420e67a485593b01210eda78')

def get_weather(city, token_open_weather):
    try:
        z = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_open_weather }")

        data = z.json()
        print(data)
    except  Exception as ex:
        print(ex)
        print("Проверьте название города")
def main():
    city = input("Введите город: ")
    get_weather(city, token_open_weather)

    if __name__ == '__main__':
        main()

bot.infinity_polling()