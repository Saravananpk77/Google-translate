from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from google_trans_new import google_translator 
import os

BOT_TOKEN = 'BOTTOKEN'

updater = Updater(1875065266:AAHhPQ6Hlp6uMttE_L_EIkw2_B3rNJ67rFE,use_context = True )

def start(updater,context):
 updater.message.reply_text('hi iam google translater I can translate any language to kannada join for more updates @lntechnical ')
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator=google_translator()
 translate_text=translator.translate(usr_msg,lang_tgt='hi')
 updater.message.reply_text(translate_text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
