from wxpy import *

class FriendsRedirector:
    def send(msg,data):
#        receiver = msg.card.accept()
        receiver = msg.sender
        print(receiver)
        receiver.set_remark_name(data['nickName'])
        receiver.send(data['info'])




