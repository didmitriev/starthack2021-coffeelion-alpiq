import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import logging

from telegram.ext import MessageHandler, Filters

from stock_price import get_current_price

# API Token: 1755647374:AAEeGfRh7eVG8Z91kPNxZhoO1-IyhXMgA3g
bot = telegram.Bot(token= '1755647374:AAEeGfRh7eVG8Z91kPNxZhoO1-IyhXMgA3g')

updater = Updater(token='1755647374:AAEeGfRh7eVG8Z91kPNxZhoO1-IyhXMgA3g', use_context=True)
dispatcher = updater.dispatcher

# log top find errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# call a function when receive a message containing /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def market(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="The market looks good! Diamond Hands! 💎💎💎 ")

def gamestop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= str(round(get_current_price('GME'), 2)) + ' $')

# should echo all non-command messages it receives
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# the core strength of the bot - send alert messages
def alert(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Dude you really need to watch out! There is a significant difference between the delivered energy and the need!")

def stock(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)




# handler for the bot
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# market handler
market_handler = CommandHandler('market', market)
dispatcher.add_handler(market_handler)

# gamestop handler
gamestop_handler = CommandHandler('gamestop', gamestop)
dispatcher.add_handler(gamestop_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()


# print(bot.get_me())

