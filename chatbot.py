import sys
import chatbotModel

def proc_rolling(bot, update):
    wooseok.sendMessage('데구르르')
    sound= firecracker()
    wooseok.sendMessage(sound)
    wooseok.sendMessage('르르르')

def proc_stop(bot, update):
    wooseok.sendMessage('봇이 잠듭니다.')
    wooseok.stop()

def firecracker():
    return '펑!'

wooseok = chatbotModel.Botwooseok()
wooseok.add_handler('rolling', proc_rolling)
wooseok.add_handler('stop', proc_stop)
wooseok.start()
