import requests

def fetch_aircraft_data(url):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        data = response.json()
        return data.get("aircraft, []")
    except requests.RequestException as e:  #hope you don't get any
        print(f"[ERROR] Failed to fetch aircraft data: {e}")
        return[]