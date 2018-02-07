import telepot
from pprint import pprint
from telepot.loop import MessageLoop
def handle(msg):
	pprint(msg)
bot = telepot.Bot('428479230:AAG2W0ZpK3Sp4HHYRskUO1w9Yu0rF_n4DQg')
print(bot.getMe())
print(MessageLoop(bot, handle).run_as_thread())
