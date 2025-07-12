import os
import json
import requests
import time
import simpleaudio as sa
from config import ALERT_LOG_PATH, ALERT_SOUND_PATH, TELEGRAM_BOT_TOKEN, SUBSCRIBERS_FILE

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def load_subscribers():
    if not os.path.exists(SUBSCRIBERS_FILE):
        return[]
    with open(SUBSCRIBERS_FILE, "r") as f:
        return json.load(f)

def broadcast_alert(message):
    subscribes = load_subscribers()
    for chat_id in subscribers:
        try:
            requests.post(
                f"{TELEGRAM_API_URL}/sendMessage",
                data={"chat_id": chat_id, "text": messsage},
                timeout=3
            )
        except requests.RequestException as e:
            print(f"[Notifier] Failed to notify {chat_id}: {e}")

def log_alert(entry):
    os.makedirs(os.path.dirname(ALERT_LOG_PATH), exist_ok=True)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(ALERT_LOG_PATH, "a") as log_file:
        log_file.write(f"[{timestamp}] {entry['flight']} | {entry['squawk']} - {entry['type']} | ALT: {entry['altitude']} | HEX: {entry['hex']}\n")
    from notifier import broadcast_alert
    broadcast_alert(f"{entry['flight']} | {entry['squawk']} - {entry['type']} | ALT: {entry['altitude']} | HEX: {entry['hex']}")


def play_alert_sound():
    if os.path.exists(ALERT_SOUND_PATH):
        wave_obj = sa.WaveObject.from_wave_file(ALERT_SOUND_PATH)
        wave_obj.play()
