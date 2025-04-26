from dotenv import load_dotenv
import os
load_dotenv()

import telebot

TOKEN = os.getenv("TOCKEN_TG")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(mess):
    bot.send_message(mess.chat.id, 'Здарова, бандиты!')

bot.polling(none_stop=True)
