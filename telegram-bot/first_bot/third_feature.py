import telepot 
token = '#####'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getUpdates(222216244+1))
