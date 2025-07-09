from collections import Counter
import os
from config import ALERT_LOG_PATH

def parse_alert_log():              # all it does is parsing
    if not os.path.exists(ALERT_LOG_PATH): return []
    lines=open(ALERT_LOG_PATH).read().splitlines()
    entries=[]
    for ln in lines:
        ts,rest=ln.split(']',1)
        ts=ts.strip('[')
        flight,info,hexc=rest.strip().split('|')
        entries.append({'timestamp':ts, 'flight':flight.strip(), 'squawk_info':info.strip(), 'hex':hexc.strip()})
    return entries

def get_squawk_stats(es):
    return Counter(e['squawk_info'].split('-')[0].strip() for e in es)

def get_recent_alerts(es,count=5):
    return es[-count:]