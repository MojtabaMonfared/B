# B
***
[![GitHub stars](https://img.shields.io/github/stars/badges/shields.svg?style=social&label=Star&maxAge=2592000?style=flat-square)](https://github.com/MojtabaMonfared/B/stargazers) [![Developer](https://img.shields.io/badge/Developer-%40MojtabaMonfared-blue.svg?style=flat-square)](https://telegram.me/MojtabaMonfared)

# What this script Can do?
with this script you can host other bots in your server! this script gives a token from user and run a script(_you should create it before use this script_) in server
# How this script do that?
this script use [`subprocess`](https://docs.python.org/2/library/subprocess.html) module and [`urllib`](https://docs.python.org/2/library/urllib.html) for getting information of token. 
and this bot use [`pyTelegramBotAPI`](https://github.com/eternnoir/pyTelegramBotAPI) library as api
# How we can run and use it?
1. first, you need to create a sample bot with any features for run in server **sample.py**
2. second, you must use this example in your code
```python
token = sys.argv[1]
bot = telebot.TeleBot(token)
```
third, you need to add your token in line 18 `B.py` and edit something in main script :)

Now you should run this script by `python B.py`
and send this command to bot `/create YOUR-TOKEN`
:trollface:
if you have any question or want to report bug
tell me in [telegram](https://telegram.me/MojtabaMonfared)
or
open an [issue](https://github.com/MojtabaMonfared/B/issues)

##GoodLuck
> MojtabaMonfared
