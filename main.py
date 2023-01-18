import telebot

bot = telebot.TeleBot('5947033600:AAF6rJihphkXcxkzAVQVYwZXkV8mUM1XDUY')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you govno?")

bot.infinity_polling()