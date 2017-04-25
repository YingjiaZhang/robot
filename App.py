#!/usr/bin/python3
import requests
from wxpy import *
import json
import logging
from TextSender import TextSender
from FriendsSender import FriendsSender
from TextRedirector import TextRedirector
from FriendsRedirector import FriendsRedirector

logging.basicConfig(level=logging.INFO)

for m in 'requests', 'urllib3':
    logging.getLogger(m).setLevel(logging.WARNING)

bot = Bot(cache_path=True)

@bot.register()
def auto_reply(msg):
    print('==============================')
    print(msg.text)
    print(msg.sender)
    print(msg.type)
    url = ''
    sender = globals()[msg.type + 'Sender']
#      redirector = globals()[msg.type + 'Redirector']
    res_data = sender.send(msg,url)
    redirector = globals()[res_data['type'] + 'Redirector']
    redirector.send(msg,res_data)
   
embed()

