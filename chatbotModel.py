import telegram
from telegram.ext import Updater,CommandHandler

class TelegramBot:
    def __init__(self,name,token):
        self.core = telegram.Bot(token)
        self.update = Updater(token)
        self.id = 727875873
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)
    
    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class Botwooseok(TelegramBot):
    def __init__(self):
        self.token = '707421517:AAHx7xaD-1iLDcGcxiBiDHo3idHiavBF-gU'
        TelegramBot.__init__(self, '우석', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd,func))

    def start(self):
        self.sendMessage('우석봇이 깨어납니다.')
        self.updater.start_polling
        self.updater.idle()