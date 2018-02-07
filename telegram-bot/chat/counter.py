import sys 
import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space


class MessageCounter(telepot.helper.ChatHandler):
	def __init__(self, *args, **kwargs):
		super(MessageCounter, self).__init__(*args, **kwargs)
		self._count = 0
	
	def on_chat_message(self, msg):
		self._count += 1
		self.sender.sendMessage(self._count)


token = '428479230:AAG2W0ZpK3Sp4HHYRskUO1w9Yu0rF_n4DQg'
bot = telepot.DelegatorBot(token, [
	pave_event_space()(
		per_chat_id(), create_open, MessageCounter, timeout=60
	),
])
MessageLoop(bot).run_as_thread()
print('Listening...')


while 1:
	time.sleep(10)
