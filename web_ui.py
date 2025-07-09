from flask import Flask, render_template, jsonify
import requests
from config import DATA_SOURCE
from squawk_utils import extract_emergencies
from history_utils import parse_alert_log, get_squawk_stats

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alerts')
def alert_page:
    return render_template('alert.html')

@app.route('/api/emergencies')
def api_emergencies():
    try:
        r = requests.get(DATA_SOURCE, timeout=3)
        r.raise_for_status()
        aircraft = r.json().get('aircraft',[])
        return jsonify(extract_emergencies(aircraft))
    except Exception as e:
        return jsonify({'error': str(e)}),500

@app.route('/api/history')
def api_history():
    entries = parse_alert_log()
    stats = get_squawk_stats(entries)
    return jsonify({'count': len(entries), 'stats': dict(status)})

@app.route('/api/alerts')
def api_alerts():
    return jsonify(parse_alert_log())

if __name__ == 'main':
    app.run(debug=True, port=5000)