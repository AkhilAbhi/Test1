#from requirements import TOKEN, USERNAME #
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, MessageHandler, Filters
import json
TOKEN ="7413073877:AAFIMuTZM0IQjANvmakArpS0sfUuOU7ohj4"
 # handlers

def start(update, context):
  """Send a message when the command /start is issued."""
  update.message.reply_text('Hi!')
def help(update, context):
  """Send a message when the command /help is issued."""
  update.message.reply_text('Help!')
  
def echo(update, context):
  """Echo the user message."""
  update.message.reply_text(update.message.text)
  
app = Flask (_name__)

def main():
  bot Bot (TOKEN)
  dp Dispatcher (bot, None, workers-0, use_context=True)
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("help", help))
  dp.add_handler(MessageHandler(Filters.text, echo))
  url=f"https://{USERNAME}.pythonanywhere.com/{TOKEN}"
  bot.delete_webhook()
  bot.set_webhook(url=url)
  
  @app.route('/'+ TOKEN, methods=['POST'])
  def webhook():
    json_string request.stream.read().decode('utf-8')
    update Update.de_json(json.loads(json_string), bot)
    dp.process_update(update)
    return 'ok', 200

- if name ='main':
  main()

