from fbchat import Client
from fbchat.models import *
import requests
import json

def get_simsimi_res(msg):
    SimsimiKey = "API-1234-abcd-1234-abcd"
    URL = "https://api.simsimi.net/v2/?text= {}&lc=en&cf=false&key={}".format(msg, SimsimiKey)
    res = requests.get(url = URL)
    res = res.text
    res = json.loads(res)
    return res["success"]

username = "overclockedpc2001@gmail.com"
password = "yyuussiiff123"

client = Client(username, password)

from fbchat import log, Client

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.sendMessage(str(get_simsimi_res(message_object.text)) + ".",
                             thread_id=thread_id, thread_type=thread_type)


client = EchoBot(username, password)
client.listen()
