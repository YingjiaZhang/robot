import requests
import json

class TextSender:
    def send(msg,url):
        sender = msg.sender
        senderInfo = sender.raw
        message = {'type':msg.type,'info':msg.text}
        data = {'senderInfo':senderInfo,'message':message}
        res = requests.post('http://localhost:3000/wechat',json = data)
#        res = requests.post('http://10.22.64.36:3000/wechat',json = data)
        return json.loads(res.text)




