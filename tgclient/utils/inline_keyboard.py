def InlineKeyboard(**kwargs):

    markup = {}
    for k, v in kwargs.items():
        markup[k] = v

    return markup
