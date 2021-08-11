import telegram
from telegram.ext import Updater,CommandHandler
from telegram import KeyboardButton,ReplyKeyboardMarkup
import logging
def start(update, context):
    update.message.reply_text('hola bienvenido!')


if __name__ == "__main__":
    updater = Updater(token="1937480308:AAFxyIBYa9awX4anvEaET-ipS87JDUxU16o",use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))
    
    updater.start_polling()
    updater.idle()

telegram.ReplyKeyboardMarkup( keyboard=True, resize_keyboard=False, one_time_keyboard=False, selective=False, input_field_placeholder=None)
    