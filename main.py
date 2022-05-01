import os
import telebot 


bot = telebot.TeleBot("5233516984:AAFJpmGmy6uk__KsxqZ1T1gN1rpi0JGnRD4")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hi Welcome To LK Developers")


@bot.message_handler(commands=["about"])
def send_message(message):
  bot.send_message(message.chat.id, "t.me/lkdeveloper")



bot.polling()
