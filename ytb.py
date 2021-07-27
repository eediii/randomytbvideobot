import random as r
import string as s
import telebot

bot = telebot.TeleBot(token='1856258753:AAGVgBurq4w7rmSWMwsG_cihQrjYMQdLQr0')

@bot.message_handler(commands=['start'])
def kod(message):
    bot.send_message(message.chat.id, f'https://www.youtube.com/watch?v={"".join(r.choice(s.ascii_letters + s.digits + "-") for i in range(11))}')

bot.polling()