import telepot
import sys
import time
from telepot.loop import MessageLoop

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type=='text':
		bot.sendMessage(chat_id, msg['text'])


TOKEN = '428479230:AAG2W0ZpK3Sp4HHYRskUO1w9Yu0rF_n4DQg'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening...')

while 1:
	time.sleep(10)
