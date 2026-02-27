import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telebot import TeleBot, types
from logic import *
from config import api_token
API_TOKEN = 'api_token'
answ1 = "none"
bot = telebot.TeleBot(api_token)

def gen_questions_markup():
    markup = types.InlineKeyboardMarkup()
    for q in questions:
        markup.add(
            types.InlineKeyboardButton(
                q["question"],
                callback_data=q["id"]   
            )
        )
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    if call.data == "help":
        keyboard = gen_questions_markup()
        bot.send_message(call.message.chat.id,
                         "Выберите вопрос:",
                         reply_markup=keyboard)

    elif call.data == "about":
            bot.send_message(call.message.chat.id, 
            """Я бот созданный для тех-поддержки сайта алиекспресс.
        "Я могу" --сказал бы я если я мог, но я просто примитивный телле-бот способствуйший отвечать на 
        заданые вопросы.""")
    else:
        for q in questions:
            if call.data == q["id"]:
                bot.send_message(call.message.chat.id, q["answer"])

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Мне нужна помощь техподдержки",
            callback_data="help"
    )
    )
    markup.add(
        types.InlineKeyboardButton(
            "Я хочу узнать что это за бот",
            callback_data="about"
    )
    )
    bot.send_message(message.chat.id,
                     "Привет, я бот техподдержки 🤚")
    bot.send_message(message.chat.id,
                     "Выберите что вы хотите узнать:",
                     reply_markup=markup)

bot.infinity_polling(none_stop=True)
