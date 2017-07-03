

def InlineQueryResult(**kwargs):

    markup = {}

    for k, v in kwargs.items():
        markup[k] = v

    return markup


def input_message_content(message_text, parse_mode=None):
    js = {}

    if message_text:
        js['message_text'] = message_text

    if parse_mode:
        js['parse_mode'] = parse_mode

    return js
