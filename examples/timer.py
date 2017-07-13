# -*- coding: utf-8 -*-
from tgclient import *
import time


token = "your token"

bot = TelegramBot(token)


@bot.command(r'^/(start)$')
def _start_command(message):

    chat_id = message['chat']['id']
    bot.sendMessage(chat_id,
                    "/set (value) (hour|minute|second)\nExample : /set 1 hour")

@bot.command(r'^/(set) (.*) (.*)$')
def delete_message(message, args=None):

    sc = 0
    if args[2] == "second":
        sc = args[1]

    elif args[2] == "minute":

        sc = Timer.min_to_sec(args[1])

    elif args[2] == "hour":

        sc = Timer.hour_to_sec(args[1])

    bot.sendMessage(message['chat']['id'], "you will receive a message in {} second".format(sc))
    def send():
        bot.sendMessage(message['chat']['id'], ":D")
    Timer(sc, send)



bot.run()
