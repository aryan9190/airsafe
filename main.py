def main_entry():
    import time
    from config import DATA_SOURCE, UPDATE_INTERVAL
    from aircraft_data import fetch_aircraft_data
    from squawk_utils import extract_emergencies
    from ui_terminal import print_header, print_emergencies
    from alert_engine import log_alert, play_alert_sound
    print_header()
    print("\n Starting AirSafe (Live Mode)")
    seen_emergencies = set()
    while True:
        aircraft = fetch_aircraft_data(DATA_SOURCE)
        emergencies = extract_emergencies(aircraft)
        print_emergencies(emergencies)

        for x in emergencies:
            key = x['hex'] + x['squawk']
            if key not in seen_emergencies:
                log_alert(x)
                play_alert_sound()
                seen_emergencies.add(key)
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    try:
        main_entry()            # importing modules locally bcoz the main_entry() will be called in dashboard.py. renamed it main_entry to avoid confusion.
    except KeyboardInterrupt:   # if i were you, i wouldn't think of doing that
        print("\n[!] Exiting...")
