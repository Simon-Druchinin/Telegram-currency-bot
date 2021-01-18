import telebot

URL_USD = 'https://ru.myfin.by/currency/usd/novosibirsk'
URL_EUR = 'https://ru.myfin.by/currency/eur/novosibirsk'
URL_CNY = 'https://ru.myfin.by/currency/cny/novosibirsk'
TOKEN = 'Your TOKEN'

BOT = telebot.TeleBot(TOKEN)

BUTTON_START = 'В начало'

BUTTON_USD = 'USD'
BUTTON_EUR = 'EUR'
BUTTON_CNY = 'CNY'

BUTTON_GET_ALL_LIST = 'Вывести весь список банков'
BUTTON_GET_ALL_ADDRESS_LIST = 'Вывести список адресов банков'
BUTTON_BEST_BUY_VALUE = 'Вывести лучший курс покупки'
BUTTON_BEST_SELL_VALUE = 'Вывести лучший курс продажи'

def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard

KEYBOARD_START = create_keyboard()
KEYBOARD_START.row(BUTTON_USD, BUTTON_EUR)
KEYBOARD_START.row(BUTTON_CNY)

KEYBOARD_CHOICE = create_keyboard()
KEYBOARD_CHOICE.row(BUTTON_GET_ALL_LIST, BUTTON_GET_ALL_ADDRESS_LIST)
KEYBOARD_CHOICE.row(BUTTON_BEST_BUY_VALUE, BUTTON_BEST_SELL_VALUE)
KEYBOARD_CHOICE.row(BUTTON_START)