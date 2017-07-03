# tgclient

#Getting Started


##Install
```sh
pip install tgclient

or

git clone https://github.com/negative23/tgclient.git
cd tgclient 

python setup.py install

```


```python
from tgclient import *

bot = TelegramBot("245100736:AAGpgrDLt1YNwsQxxxxxxxxxxxxxxxxxxxx")


@bot.message("text")
def text(message):
    print(message) 
    # {'message_id': 6577, 'from': {'id': 68747297, ... ...
    
bot.run()

```

