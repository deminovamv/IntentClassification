from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import main


class TelegramChecker:  

    def __init__(self):
        self.updater = Updater(settings.API_KEY, use_context= True, request_kwargs= main.PROXY)
        self.dp = self.updater.dispatcher
   
   
    def run(self):
        logging.info('START')
        self.dp.add_handler(CommandHandler("start", self.start_command))
        self.dp.add_handler(MessageHandler(Filters.text, self.process))
        self.updater.start_polling()
        self.updater.idle()


    def start_command(self,update,context):
        print("start")
        name = update.message.chat.first_name
        update.message.reply_text(f'Привет, {name} 😊!')
    
    
    def process(self,update, context):
        text= update.message.text
        update.message.reply_text(text)