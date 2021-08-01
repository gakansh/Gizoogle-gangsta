import requests
import json
import re
import bs4
from urllib import parse
import argparse


def text(input_text: str) -> str:
    params = {"translatetext": input_text}
    target_url = "http://www.gizoogle.net/textilizer.php"
    resp = requests.post(target_url, data=params)
    # the html returned is in poor form normally.
    soup_input = re.sub(
        "/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text)
    soup = bs4.BeautifulSoup(soup_input, "lxml")
    giz = soup.find_all(text=True)
    giz_text = giz[37].strip("\r\n")  # Hacky, but consistent.
    print(giz_text)
    return giz_text




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

def translate(msg):
    gurl = "http://www.gizoogle.net/textilizer.php"
    



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
            reply = text(msg)
            sendmessage(reply, frm)
