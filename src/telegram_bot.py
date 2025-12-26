import yaml
import requests

with open("config/config.yaml") as f:
    cfg = yaml.safe_load(f)
bot_token = cfg['telegram']['bot_token']
chat_id = cfg['telegram']['chat_id']

def send_signal(signal):
    text = f"Signal: {signal['action']}\nEntry: {signal['entry']}\nStop: {signal['stop']}\nTarget: {signal['target']}"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)
