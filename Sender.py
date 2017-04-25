import requests
import json
from wxpy import *
class TextSender:
    def getSender(msg):
        return msg.sender

    def isGroup(msg):
        return isinstance(msg.chat,Group)
  
    def getMessage(msg):
        if isGroup(msg):
            return {'type':msg.type,'info':msg.text,'owner':msg.member.raw}
        return {'type':msg.type,'info':msg.text,'owner':msg.sender.raw}

    def getSenderInfo(msg)
        return msg.sender.raw
    
    def send(msg):
        data = {'senderInfo':getSenderInfo(msg),'message':getMessage(msg)}
#        res = requests.post('http://localhost:3000/wechat',json = data)
        res = requests.post('http://10.22.64.36:3000/wechat',json = data)
        return json.loads(res.text)




