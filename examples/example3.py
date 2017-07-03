# -*- coding: utf-8 -*-
from tgclient import *
import time


token = "your token"

bot = TelegramBot(token)


@bot.command(r'^/(deleteMessage)')
def delete_message(message):

    req = bot.sendMessage(message['chat']['id'], ":D Test!")

    # req return : https://core.telegram.org/bots/api#message

    time.sleep(1)

    if 'message_id' in req:
        bot.deleteMessage(message['chat']['id'], req['message_id'])



bot.run()
