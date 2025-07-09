import argparse
from main import main_entry as cli_monitor
from ui_dashboard import dashboard_loop
import web_ui
from history_utils import parse_alert_log, get_squawk_stats, get_recent_alerts

def run_web():
    web_ui.app.run(port=5000)

def run_cli():
    cli_monitor()

def run_dashboard():
    dashboard_loop()

def run_history():
    entries=parse_alert_log()
    stats=get_squawk_stats(entries)
    recent=get_recent_alerts(entries)
    print("\n Emergency Squawk Stats:")
    for sq, cnt in stats.items(): print(f"  {sq}: {cnt} times")
    print("\n Recent Alerts:")
    for e in recent: print(f"  [{e['timestamp']}] {e['flight']} | {e['squawk_info']} | HEX: {e['hex']}")

def main():
    parser = argparse.ArgumentParser(description='Squawk Sentinel Unified Launcher')
    parser.add_argument('--mode', choices=['cli', 'dashboard', 'web', 'history'], default='cli')
    args = parser.parse_args()
    if args.mode=='cli': run_cli()
    elif args.mode=='dashboard': run_dashboard()
    elif args.mode=='web': run_web()
    elif args.mode=='history': run_history()

if __name__=='__main__':main()