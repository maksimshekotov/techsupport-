import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telebot import TeleBot, types
from logic import *
from config import api_token
API_TOKEN = 'api_token'
answ1 = "none"
bot = telebot.TeleBot(api_token)

def info(message):
    bot.send_message(message.chat.id, """Я бот созданный для тех-поддержки,
    Я     
    """)

def gen_inline_markup(rows):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    for row in rows:
        markup.add(types.InlineKeyboardButton(row, callback_data=row))
    return markup

def example():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        keyboard = gen_inline_markup(["Choice 1", "Choice 2"])
        bot.send_message(message.chat.id, "Please choose:", reply_markup=keyboard)
    # Handle button presses
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        if call.data == "Choice 1":
            bot.answer_callback_query(call.id, "You clicked Choice 1")
            bot.send_message(call.message.chat.id, "You selected option 1!")

        elif call.data == "Choice 2":
            bot.answer_callback_query(call.id, "You clicked Choice 2")
            bot.send_message(call.message.chat.id, "You selected option 2!")

@bot.message_handler(commands=['start'])
def start(message):
    question1 = gen_inline_markup(["Мне нужна помошь техподдержки", "Я хочу узнать что зачем этот бот"])
    bot.send_message(message.chat.id, "Привет, я бот техподдержки сайта алиекспресс🤚")
    bot.send_message(message.chat.id, "Выбирите чтоб вы потом напишу", reply_markup=question1)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "Мне нужна помошь техподдержки":
        bot.answer_callback_query(call.id, "You clicked Choice 1")
        bot.send_message(call.message.chat.id, "You selected option 1!")

    elif call.data == "Я хочу узнать что зачем этот бот":
        bot.send_message(call.message.chat.id, "Что умеет этот бот:")
        
bot.infinity_polling(none_stop=True)
