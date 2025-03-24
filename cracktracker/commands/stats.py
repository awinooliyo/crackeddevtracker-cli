import typer
from cracktracker.db import get_db
from rich.console import Console
from collections import defaultdict
from datetime import datetime

app = typer.Typer()
console = Console()

@app.command()
def summary():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp FROM logs")
    rows = cursor.fetchall()
    conn.close()

    per_day = defaultdict(int)
    for row in rows:
        date = row[0][:10]
        per_day[date] += 1

    console.print(f"📊 Total Logs: [bold green]{len(rows)}[/bold green]")
    console.print(f"📅 Active Days: [bold blue]{len(per_day)}[/bold blue]")

    # Optional: Print streaks or daily breakdown later
