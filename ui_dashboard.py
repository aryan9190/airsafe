from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from datetime import datetime
from config import DATA_SOURCE, UPDATE_INTERVAL
from aircraft_data import fetch_aircraft_data
from squawk_utils import extract_emergencies

console = Console()

def generate_table(emergencies):
    table = Table(title="Live Emergency Monitor", expand=True)
    table.add_column("Flight", style="cyan", no_wrap=True)
    table.add_column("Squawk", style="yellow")
    table.add_column("Type", style="magenta")
    table.add_column("Altitude", style="green")
    table.add_column("Hex Code", style="blue")
    if not emergencies:
        table.add_row("-","-","No emergencies","-","-")
    else:
        for e in emergencies:
            style = "bold red" if e["squawk"] in ["7500","7600","7700"] else "bold yellow"
            table.add_row(e["flight"], f"[{style}]{e['squawk']}[/{style}]", e["type"], str(e["altitude"]), e["hex"])
    return table

def dashboard_loop():
    with Live(refresh_per_second=1, console=console) as live:
        while True:
            aircraft = fetch_aircraft_data(DATA_SOURCE)
            emergencies = extract_emergencies(aircraft)
            table = generate_table(emergencies)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            header = Panel(Text("AirSafe UI Dashboard", style="bold green"))
            footer = Panel(Text(f"Last Update: {timestamp}", style="bold blue"))
            layout = Table.grid(expand=True)
            layout.add_row(header)
            layout.add_row(table)
            layout.add_row(footer)
            live.update(layout)

if __name__ == '__main__':
    from time import sleep
    try:
        dashboard_loop()
    except KeyboardInterrupt:
        console.print("\n[bold red] Exiting dashboard...")