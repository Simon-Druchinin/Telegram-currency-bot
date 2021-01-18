from settings.SETTINGS import *

import telebot

from parse.Parse import Parse
from parse.data import Data, Data_address

currency_type = ''

@BOT.message_handler(commands=['start'])
def start_message(message):
    BOT.send_message(message.chat.id, 'Выберете интересующую вас валюту', reply_markup=KEYBOARD_START)

@BOT.message_handler(content_types=['text'])
def get_text_messages(message):

    global site, values, currency_type

    if message.text == BUTTON_USD:
        currency_type = 'USD'

        site = Parse(URL_USD).get_content()
        site_page_2 = Parse(URL_USD + '?page=2').get_content()

        for item in site_page_2:
            site.append(item)

        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_EUR:
        currency_type = 'EUR'

        site = Parse(URL_EUR).get_content()
        site_page_2 = Parse(URL_EUR + '?page=2').get_content()
        
        for item in site_page_2:
            site.append(item)

        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_CNY:
        currency_type = 'CNY'

        site = Parse(URL_CNY).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?', reply_markup=KEYBOARD_CHOICE)
    
    elif message.text == BUTTON_GET_ALL_LIST:
        BOT.send_message(message.chat.id, values.get_all_list(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_BEST_BUY_VALUE:
        BOT.send_message(message.chat.id, values.get_best_buy_value(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_BEST_SELL_VALUE:
        BOT.send_message(message.chat.id, values.get_best_sell_value(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_START:
        start_message(message)

    elif message.text == BUTTON_GET_ALL_ADDRESS_LIST:
        make_inline_keyboard(message, values.get_data_names())

    else:
        BOT.send_message(message.chat.id, 'Я тебя не понимаю! Напиши, пожалуйста, /start')

def get_address_list(currency_type):
    bank_names = []

    if currency_type == 'USD':

        site = Parse(URL_USD).get_all_banks_address()
        site_page_2 = Parse(URL_USD + '?page=2').get_all_banks_address()

        for item in site_page_2:
            site.append(item)

        values_address = Data_address(site)
        bank_names = values_address.get_bank_names()
    
    elif currency_type == 'EUR':
    
        site = Parse(URL_EUR).get_all_banks_address()
        site_page_2 = Parse(URL_EUR + '?page=2').get_all_banks_address()

        for item in site_page_2:
            site.append(item)

        values_address = Data_address(site)
        bank_names = values_address.get_bank_names()
    
    elif currency_type == 'CNY':
    
        site = Parse(URL_CNY).get_all_banks_address()

        values_address = Data_address(site)
        bank_names = values_address.get_bank_names()

    return bank_names

@BOT.message_handler(content_types=['text'])
def make_inline_keyboard(message, names):
    bank_names = get_address_list(currency_type)
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)

    i = 0
    while i <= len(bank_names):
        if i <= len(bank_names)-1 and names[i] == 'Тинькофф Банк':
            names.pop(i)
        elif i + 1 <= len(bank_names)-1 and names[i+1] == 'Тинькофф Банк':
            names.pop(i+1)
        elif i + 2 <= len(bank_names)-1 and names[i+2] == 'Тинькофф Банк':
            names.pop(i+2)
        else:
            if i <= len(bank_names)-1:
                button_bank_name = telebot.types.InlineKeyboardButton(names[i], callback_data=f'{bank_names[i]}')
            if i + 1 <= len(bank_names)-1:
                button_bank_name_2 = telebot.types.InlineKeyboardButton(names[i+1], callback_data=f'{bank_names[i+1]}')
            if i + 2 <= len(bank_names)-1:
                button_bank_name_3 = telebot.types.InlineKeyboardButton(names[i+2], callback_data=f'{bank_names[i+2]}')

            if i + 2 <= len(bank_names)-1:
                markup.add(button_bank_name, button_bank_name_2, button_bank_name_3)

            elif i + 1 <= len(bank_names)-1:
                markup.add(button_bank_name, button_bank_name_2)

            elif i <= len(bank_names)-1:
                markup.add(button_bank_name)

            i += 3

    BOT.send_message(message.chat.id, 'Выберете нужный вам банк', reply_markup=markup)

@BOT.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    bank_names = get_address_list(currency_type)
    try:
        if call.message:
            if call.data in bank_names:
                bank_name = call.data
                message = get_bank_address(bank_name, currency_type)
            BOT.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup=None)
    except Exception as e:
        print(repr(e))

def get_bank_address(bank_name, currency_type):
    message = ''

    if currency_type == 'USD':
    
        site = Parse(URL_USD).get_all_banks_address()
        site_page_2 = Parse(URL_USD + '?page=2').get_all_banks_address()

        for item in site_page_2:
            site.append(item)

        values_address = Data_address(site)
    
    elif currency_type == 'EUR':
    
        site = Parse(URL_EUR).get_all_banks_address()
        site_page_2 = Parse(URL_EUR + '?page=2').get_all_banks_address()

        for item in site_page_2:
            site.append(item)

        values_address = Data_address(site)
    
    elif currency_type == 'CNY':
    
        site = Parse(URL_CNY).get_all_banks_address()

        values_address = Data_address(site)

    message = values_address.get_your_bank_address(bank_name)

    return message
    
BOT.polling()