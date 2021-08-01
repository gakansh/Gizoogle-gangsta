from bot import telegram_bot

update_id = None
def make_reply(msg):
    reply = "Okazz"
    return reply
while True:
    print "......"
    updates = bot.get_updates(offset=update_id)
    updates.updates["result"]
    if(updates)
        for item in updates:
            update_id = item["update_id"]

            try:
                msg = item["message"]["text"]
            except:
                msg=None

            frm = item["message"]["from"]["id"]
            reply = make_reply(msg)
            bot.send_message(reply,frm)
