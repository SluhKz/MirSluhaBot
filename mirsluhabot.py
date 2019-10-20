# -*- coding: utf-8 -*-
import telebot
import config
import adresa

from telebot.types import Message
bot = telebot.TeleBot(config.TOKEN2)
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
@bot.message_handler(commands=['Hello'])
def cmd_start(message):
    bot.send_message(message.from_user.id, 'Привет')


keyboardMenu = telebot.types.ReplyKeyboardMarkup(True)
keyboardMenu.row('Контакты')
keyboardMenu.row('Новости')
@bot.message_handler(commands=['start'])
def text_message(message):

    bot.send_message(message.chat.id, 'Добро пожаловать в аккаунт компании "Мир слуха"!\nВыберите один из пунктов меню!', reply_markup=keyboardMenu)
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################

keyboardContacts = telebot.types.ReplyKeyboardMarkup(True)
keyboardContacts.row('Алматы', 'Астана', 'Актау')
keyboardContacts.row('Атырау', 'Шамкент', 'Караганда')
keyboardContacts.row('Назад')
@bot.message_handler(content_types=['text'])
def text_message(message):
    markup_close = telebot.types.ReplyKeyboardRemove()

    #КОНТАКТЫ============КОНТАКТЫ============КОНТАКТЫ============КОНТАКТЫ============КОНТАКТЫ===========================
    if message.text == 'Контакты':

        bot.send_message(message.chat.id, 'Пожалуйста, выберите Ваш город!', reply_markup=keyboardContacts)

    elif message.text == 'Алматы':
        bot.send_message(message.chat.id, adresa.Almaty)
    elif message.text == 'Астана':
        bot.send_message(message.chat.id, adresa.Astana)
    elif message.text == 'Актау':
        bot.send_message(message.chat.id, adresa.Aktau)
    elif message.text == 'Атырау':
        bot.send_message(message.chat.id, adresa.Atyrau)
    elif message.text == 'Шамкент':
        bot.send_message(message.chat.id, adresa.Shymkent)
    elif message.text == 'Караганда':
        bot.send_message(message.chat.id, adresa.Karaganda)
    #Новости================Новости================Новости================Новости================Новости================
    elif message.text == 'Новости':

        bot.send_message(message.chat.id, 'Чтобы не пропустить новости и акции, подпишитесь на канал Центра "Мир Слуха" https://t.me/mirsluha')
    #Акции============Акции============Акции============Акции============Акции============Акции============Акции========
    elif message.text == 'Акции':

        bot.send_message(message.chat.id, 'АКЦИИ!!!!!!!!!!!!!!!!!!!!')
    #Запись на приём============Запись на приём============Запись на приём============Запись на приём===================
    elif message.text == 'Записаться на приём':

        bot.send_message(message.chat.id, 'Пожалуйста, введите Ваше ФИО и номер контактного телефона! Для возврата меню нажммите /start', reply_markup=markup_close) and (868353437, message, text_message)

    elif message.text == 'Назад':

        bot.send_message(message.chat.id, 'ГЛАВНОЕ МЕНЮ', reply_markup=keyboardMenu)
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################

bot.polling()
