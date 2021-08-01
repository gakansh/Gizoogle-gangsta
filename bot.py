import requests
import json



def getupdates(offset):
    url = "https://api.telegram.org/bot1902634806:AAHa59sXh5xgMmeXjyZxXZWMcKLG0SnXFaU" + "/getUpdates?timeout=100"
    if offset is not None:
        url = url + "&offset={}".format(offset + 1)
    r = requests.get(url)
    return json.loads(r.content)


def sendmessage(msg, char_id):
    url = "https://api.telegram.org/bot1902634806:AAHa59sXh5xgMmeXjyZxXZWMcKLG0SnXFaU" + "/sendMessage?text={}&chat_id={}".format( msg,char_id)
    if msg is not None:
        requests.get(url)


update_id = None


def make_reply():
    reply = "Okazz"
    return reply


update_id = None
while True:
    print("......")
    updates = getupdates(update_id)
    updates = updates['result']
    if(updates):
        for item in updates:
            update_id = item["update_id"]
            try:
                msg = item["message"]["text"]
            except:
                msg = None
            frm = item["message"]["from"]["id"]
            reply = make_reply()
            sendmessage(msg, frm)
