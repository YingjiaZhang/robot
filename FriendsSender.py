import requests
import json
from wxpy import *
class FriendsSender:
    def send(msg,url):
        sender = msg.card.accept()
        senderInfo = sender.raw
        message = {'type':msg.type,'info':msg.text,'owner':senderInfo}
        data = {'senderInfo':senderInfo,'message':message}
        res = requests.post('http://localhost:3000/wechat',json = data)
#        res = requests.post('http://10.22.64.36:3000/wechat',json = data)
        return json.loads(res.text)




