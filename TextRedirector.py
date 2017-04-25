from wxpy import *

class TextRedirector:
    def send(msg,data):
        reciver = msg.sender
        if isinstance(msg.chat,Friend):
            reciver.send(data['info'])




