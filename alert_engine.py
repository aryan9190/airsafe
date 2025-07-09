import os
import time
import simpleaudio as sa
from config import ALERT_LOG_PATH, ALERT_SOUND_PATH

def log_alert(entry):
    os.makedirs(os.path.dirname(ALERT_LOG_PATH), exist_ok=True)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(ALERT_LOG_PATH, "a") as log_file:
        log_file.write(f"[{timestamp}] {entry['flight']} | {entry['squawk']} - {entry['type']} | ALT: {entry['altitude']} | HEX: {entry['hex']}\n")

def play_alert_sound():
    if os.path.exists(ALERT_SOUND_PATH):
        wave_obj = sa.WaveObject.from_wave_file(ALERT_SOUND_PATH)
        wave_obj.play()
