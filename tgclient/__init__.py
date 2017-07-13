from .Client import TelegramBot
from .utils.inline_result import InlineQueryResult, input_message_content
from .utils.inline_keyboard import InlineKeyboard
from .utils.photosize import *
from .timer import Timer

__all__ = [
    'TelegramBot',
    'InlineQueryResult',
    'InlineKeyboard',
    'large_photo',
    'small_photo',
    'Timer'
]
