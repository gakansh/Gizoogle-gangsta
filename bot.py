import request
import json
import configparser as cfg

class telegram_bot():
    """docstring for telegram_bot."""

    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)




    def get_updates(self,offset=None):
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url = self.base + "/getUpdates?timeout=100&offset={}".format(offset + 1)
        r=request.get(url);
        return json.loads(r.content)

    def send_message(self,msg , char_id):
        url =    self.base + "/sendMessage?char_id={}&text={}".format(char_id,msg)
        if msg is not None:
            request.get(url)

    def read_token_from_config_file(config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('cred' , 'token')

        
