import os
import time
from config import ALERT_LOG_PATH, ALERT_SOUND_PATH
from playsound import playsound

logged=set()

def log_alert(entry):
    os.makedirs(os.path.dirname(ALERT_LOG_PATH), exist_ok=True)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(ALERT_LOG_PATH, "a") as log_file:
        log_file.write(f"[{timestamp}] {entry['flight']} | {entry['squawk']} - {entry['type']} | ALT: {entry['altitude']} | HEX: {entry['hex']}\n")

def play_alert_sound():                 # make sure the file is there and hope there is no alert sound when you run this program
    if os.path.exists(ALERT_SOUND_PATH):
        playsound(ALERT_SOUND_PATH)