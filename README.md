# AirSafe

AirSafe is a real-time aircraft emergency detection and alerting system powered by RTL-SDR and [dump1090](https://github.com/flightaware/dump1090). It monitors aircraft squawk codes to detect life-threatening aviation emergencies such as hijacks, radio failures, or general distress situations. Built for Waveband (YSWS) by Hack Club.

This project was inspired by the tragic Air India Express crash near Ahmedabad and aims to build public awareness and early response capability.

## Features

- Real-time monitoring of ADS-B aircraft data via dump1090
- Detects emergency squawk codes: 7500, 7600, 7700
- Terminal UI with aircraft information and ASCII plane art
- Plays an alert sound and logs all incidents to alerts.log
- Optional web UI for browser-based monitoring
- Dark mode and emergency list viewer in the web dashboard
- Ready for public display or emergency broadcast station integration

## How It Works

AirSafe connects to your local dump1090 server (`localhost:8080/data/aircraft.json`) and checks all nearby aircraft for emergency squawk codes. If one is detected, it:

- Logs the incident to a timestamped log file
- Plays an audible alarm
- Displays the emergency in both terminal and web UIs

## Install PIP
```
pip install airsafe
```

## Requirements

- Python 3.8+
- dump1090 running on your local machine
- RTL-SDR dongle and antenna
- Python libraries listed in requirements.txt

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

To begin using AirSafe, ensure dump1090 is running locally and your RTL-SDR dongle is connected.

Start dump1090:
```bash
./dump1090 --interactive --net
```

Run the AirSafe terminal interface:
```bash
python main.py
```

Run the AirSafe terminal dashboard:
```bash
python ui_dashboard.py
```

Launch the web dashboard:
```bash
python web_ui.py
```

Access the web dashboard at:
```
http://localhost:5000
```

The terminal UI will show emergencies as they occur, and the web dashboard will display a log-based summary.

## Supported Squawk Codes

AirSafe monitors the following codes that represent critical aircraft situations:

| Code  | Meaning             |
|-------|----------------------|
| 7500  | Hijack               |
| 7600  | Radio Failure        |
| 7700  | General Emergency    |
| 0000  | Unassigned Code      |
| 1200  | VFR (Normal Flight)  |

This list is extendable in `squawk_utils.py`.

## Logs

All emergencies are logged with timestamps to:

```
data/alerts.log
```

Each entry includes:
- Flight number (if available)
- Squawk code
- Emergency type
- Altitude
- Aircraft hex code

## License

This project is distributed under the MIT License. See [LICENSE](./LICENSE) for details.
