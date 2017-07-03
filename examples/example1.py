# -*- coding: utf-8 -*-
from tgclient import *

token = "your token"

bot = TelegramBot(token)


@bot.command(r'^/(start)$')
def start(message, args):

    bot.sendMessage(message['chat']['id'], "Hello", reply_markup={
        'inline_keyboard': [
            [
                InlineKeyboard(text="Hello", callback_data="1"),
                InlineKeyboard(text="Hello", callback_data="2")
            ],
            [
                InlineKeyboard(text="Hi", callback_data="3"),
                InlineKeyboard(text="Hi", callback_data="4")
            ]
        ]
    })


@bot.command(r'^/(pin)')
def pin_message(message):
    if message['reply_to_message']:
        reply = message['reply_to_message']

        if message['chat']['type'] == 'supergroup':

            bot.pinChatMessage(message['chat']['id'], reply['message_id'])



@bot.inline_query()
def inline_query(inline):

    bot.answerInlineQuery(inline['id'], results=[

        InlineQueryResult(type="article", id='1', input_message_content=input_message_content("Hello"),
                          title="Hi")
    ])

@bot.callback_query()
def callback_query(callback_query):
    bot.answerCallbackQuery(
        callback_query['id'], 'Hello'
    )

bot.run(report_http_errors=False)
