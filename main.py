
import telebot
from telebot import types
from dotenv import dotenv_values

config = dotenv_values(".env")
TOKEN = config["TOKEN"]

bot = telebot.TeleBot(TOKEN)

# دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "به ربات دانلود فیلم خوش اومدی 🎬\n\n"
        "برای دانلود فیلم عضو بخش membership شو 👇\n"
        "/membership"
    )

# دستور /membership
@bot.message_handler(commands=['membership'])
def membership(message):
    bot.reply_to(
        message,
        "💳 برای خرید اشتراک با ادمین تماس بگیر:\n@sajadmyy"
    )

if __name__ == "__main__":
    bot.infinity_polling()