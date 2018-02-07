import sys
import time
import random
import traceback
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space



class Player(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self._answer = random.randint(0,99)

    def _hint(self, answer, guess):
        if answer > guess:
            return 'larger'
        else:
            return 'smaller'

    def open(self, initial_msg, seed):
        self.sender.sendMessage('Guess my number')
        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type != 'text':
            self.sender.sendMessage('Give me a number, please.')
            return

        try:
           guess = int(msg['text'])
        except ValueError:
            self.sender.sendMessage('Give me a number, please.')
            return

        # check the guess against the answer ...
        if guess != self._answer:
            # give a descriptive hint
            hint = self._hint(self._answer, guess)
            self.sender.sendMessage(hint)
        else:
            self.sender.sendMessage('Correct!')
            self.close()

    def on__idle(self, event):
        self.sender.sendMessage('Game expired. The answer is %d' % self._answer)
        self.close()


TOKEN = '428479230:AAG2W0ZpK3Sp4HHYRskUO1w9Yu0rF_n4DQg'

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, Player, timeout=10),
])
MessageLoop(bot).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)