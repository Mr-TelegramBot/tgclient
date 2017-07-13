# tgclient

Telegram Api Client


# Getting Started


## Install
```sh
pip install tgclient

or

git clone https://github.com/negative23/tgclient.git
cd tgclient 

python setup.py install

```


## getupdates example

```python
from tgclient import *

bot = TelegramBot("245100736:AAGpgrDLt1YNwsQxxxxxxxxxxxxxxxxxxxx")


@bot.message("text")
def text(message):
    print(message)
    # {'message_id': 6577, 'from': {'id': 68747297, ... ...

bot.run()

```

## command handler

```python
from tgclient import *

bot = TelegramBot("245100736:AAGpgrDLt1YNwsQxxxxxxxxxxxxxxxxxxxx")


@bot.command(r'^(/echo) (.*)')
def text(message, args):
    # args[2] two argument of command
    bot.sendMessage(message['chat']['id'], args[1])

bot.run()

