import os
from colorama import Fore, Style, init  # refer colorama-manual if you need do not have anything else to read.
init(autoreset=True)
ASCII_PATH = "assets/plane.txt"

def print_header():
    if os.path.exists(ASCII_PATH):
        with open(ASCII_PATH) as f:
            print(Fore.CYAN+f.read())
    print(Fore.GREEN + Style.BRIGHT + "AirSafe UI - Live Emergency Monitor")
    print("Data Source:", Fore.YELLOW + "http://localhost:8080")
    print("===============================================") # this looks good on a terminal with font-size 14 on a 1920x1080 screen (standard). adjust if necessary.

def print_emergencies(emergencies):
    print("\n"+ Fore.MAGENTA+"Detected Emergencies:")
    if not emergencies:
        print(Fore.BLUE + "None at this time.")     # hope you always see this line
    for e in emergencies:
        print(Fore.RED + f" ⚠ {e['flight']} | {e['squawk']} - {e['type']} | ALT: {e['altitude']} | HEX: {e['hex']}")   #everything is good if the screen doesn't have any RED on it until you're testing