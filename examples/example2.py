# -*- coding: utf-8 -*-

"""
Input Files example

InputFile : open('path', 'rb') or string file_id

"""

from tgclient import *

token = "your token"

bot = TelegramBot(token)


@bot.command("^/(photo)$")
def on_photo_command(message):

    bot.sendPhoto(message['chat']['id'], photo=open("media/406.jpg", 'rb'), caption=":D")

@bot.command("^/(document)$")
def on_document_command(message):

    bot.sendDocument(message['chat']['id'], document=open('media/document.txt', 'rb'))



@bot.message('photo')
def on_photo(message):
    photosize = message['photo']

    bot.sendPhoto(message['chat']['id'],
                  large_photo(photosize)['file_id'],
                  'Hello :D')
