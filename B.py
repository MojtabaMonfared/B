# -*- coding: utf-8 -*-
"""
# Author: MojtabaMonfared
"""
import telebot
import sys
import os
import urllib as ulib
from telebot import types
import re
import json
import requests
import subprocess

markupstart = types.InlineKeyboardMarkup()
markupstart.add(types.InlineKeyboardButton('About', callback_data='about'))

token = '[YOUR-TOKEN-HERE]'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """


    		[YOUR START MESSAGE HERE]

    	""", reply_markup=markupstart, parse_mode="Markdown", disable_web_page_preview=True)

@bot.message_handler(commands=['create'])
def create(message):
	try:
		token = message.text.split(' ')[1]
		url = 'https://api.telegram.org/bot{}/getMe'.format(token)
		r = requests.get(url)
		jdat = r.json()
		username = jdat["result"]["username"]
		subprocess.Popen("python sample.py {}".format(token),shell=True) # You Need to Create Sample Bot To start
		bot.send_message(message.chat.id, "Connected to @{}".format(username))
	except IndexError:
		bot.send_message(message.chat.id, "Token Error")

@bot.callback_query_handler(func=lambda call: call.data == 'about')
def btn_pass(call):
    bot.answer_callback_query(call.id, text="""👤 Developer: @MojtabaMonfared
📢 Channel: @BotForest
""", show_alert=True)

bot.polling(none_stop=True)
"""
Licenced under GNU AGPL v3
"""