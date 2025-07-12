import os
import json
import requests
from flask import Flask, request

TELEGRAM_TOKEN = ""
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
SUBSCRIBERS_FILE = "data/subscribers.json"

app = Flask(__name__)

os.makedirs("data", exist_ok=True)

if os.path.exists(SUBSCRIBERS_FILE):
    with open(SUBSCRIBERS_FILE, "w") as f:
        subscribers = json.load(f)
else:
    subscribers=[]

def save_subscribers():
    with open(SUBSCRIBERS_FILE) as f:
        json.dump(subscribers, f)
        

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text","")

        if text.lower() in ["/start", "/subscribe"]:
            if chat_id not in subscribers:
                subscribers.append(chat_id)
                save_subscribers()
                send_message(chat_id, "You are now subscribed to AirSafe alerts!")

            else:
                send_message(chat_id, "You are already subscribed.")
        
        return "ok"
    
def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    requests.post(url, json={"chat_id":chat_id,"text":text})

def broadcast_alert(message):
    for chat_id in subscribers:
        send_message(chat_id, message)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# To run the webhook locally:
# ngrok http 8000 and then set webhook via:
# curl -X POST "https://api.telegram.org/bot<token>/setWebhook?url=<ngrok_url>/webhook"