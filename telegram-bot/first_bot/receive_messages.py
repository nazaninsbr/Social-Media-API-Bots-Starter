import telepot
from pprint import pprint
from telepot.loop import MessageLoop
def handle(msg):
	pprint(msg)
bot = telepot.Bot('#######')
print(bot.getMe())
print(MessageLoop(bot, handle).run_as_thread())
