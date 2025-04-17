import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Работа с администрацией"), KeyboardButton("Махинации/логи"))
    markup.add(KeyboardButton("Для следующих"))
    markup.add(KeyboardButton("Форум"))
    return markup

def admin_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Поиск твинков", "Поиск аккаунта(-ов)", "Проверка активности акк.")
    markup.row("Проверка безопасности", "Проверка онлайна по нику", "История трейдов")
    markup.add("Вернуться в главное меню")
    return markup

def logs_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Поиск Названия/ID предмета", "Статистика действий", "Средняя цена предмета")
    markup.row("Средняя цена авто", "Махинации через мусорки")
    markup.add("Вернуться в главное меню")
    return markup

def next_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Проверка безопасности", "Проверка онлайна", "Лог игрока во фракции")
    markup.row("Лог денег в организации", "Статистика игрока", "Проверка УДО")
    markup.row("Игроки в организации", "Лог общака", "Лог слётов")
    markup.row("Лог выдачи выговоров", "Лог выдачи розыска", "Лог выдачи мед.карт")
    markup.add("Вернуться в главное меню")
    return markup

def forum_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Статистика жалоб")
    markup.add("Вернуться в главное меню")
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Выберите нужный раздел:", reply_markup=main_menu())

@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    if message.text == "Работа с администрацией":
        bot.send_message(message.chat.id, "Работа с администрацией:", reply_markup=admin_menu())
    elif message.text == "Махинации/логи":
        bot.send_message(message.chat.id, "Махинации/логи:", reply_markup=logs_menu())
    elif message.text == "Для следующих":
        bot.send_message(message.chat.id, "Для следующих:", reply_markup=next_menu())
    elif message.text == "Форум":
        bot.send_message(message.chat.id, "Форум:", reply_markup=forum_menu())
    elif message.text == "Вернуться в главное меню":
        bot.send_message(message.chat.id, "Главное меню:", reply_markup=main_menu())
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите вариант из меню.")

if __name__ == "__main__":
    bot.infinity_polling()
