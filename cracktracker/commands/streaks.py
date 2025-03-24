import typer
from cracktracker.db import get_db
from rich import print
from datetime import datetime, timedelta

app = typer.Typer()

@app.command()
def show():
    """Show your current and longest log streak"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp FROM logs ORDER BY timestamp ASC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("[yellow]You have no logs yet. Start with:[/yellow] crack add log \"Did some work\"")
        return

    # Parse timestamps
    dates = sorted([datetime.fromisoformat(ts[0]).date() for ts in rows])
    unique_days = sorted(set(dates))

    current_streak = 1
    longest_streak = 1

    for i in range(1, len(unique_days)):
        delta = (unique_days[i] - unique_days[i - 1]).days
        if delta == 1:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        elif delta > 1:
            current_streak = 1

    last_log = unique_days[-1]
    today = datetime.today().date()

    if (today - last_log).days > 1:
        current_streak = 0

    print("\n🔥 [bold]Crack Streaks[/bold]")
    print(f"📅 Last log date: [cyan]{last_log}[/cyan]")
    print(f"🔥 Current streak: [green]{current_streak}[/green] day(s)")
    print(f"🏆 Longest streak: [blue]{longest_streak}[/blue] day(s)")
