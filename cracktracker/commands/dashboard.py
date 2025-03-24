import typer
from cracktracker.db import get_db
from datetime import datetime, timedelta
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def show():
    """Show the CrackTracker overview dashboard"""
    conn = get_db()
    cursor = conn.cursor()

    # ---------------------
    # ✅ Today’s Logs
    today_str = datetime.now().date().isoformat()
    cursor.execute("SELECT content FROM logs WHERE timestamp LIKE ?", (f"{today_str}%",))
    logs_today = cursor.fetchall()

    logs_text = "\n".join(f"• {row[0]}" for row in logs_today) or "No logs yet. Run: crack add log"

    # ---------------------
    # 🔥 Streaks
    cursor.execute("SELECT timestamp FROM logs ORDER BY timestamp ASC")
    all_logs = cursor.fetchall()
    dates = sorted(set(datetime.fromisoformat(row[0]).date() for row in all_logs))
    streak, longest = 0, 0
    for i in range(1, len(dates)):
        delta = (dates[i] - dates[i - 1]).days
        if delta == 1:
            streak += 1
            longest = max(longest, streak + 1)
        elif delta > 1:
            streak = 0
    if dates and (datetime.today().date() - dates[-1]).days > 1:
        streak = 0

    # ---------------------
    # 🎯 Goals
    cursor.execute("SELECT goal, completed FROM goals ORDER BY id DESC LIMIT 3")
    goals = cursor.fetchall()

    # ---------------------
    # 🧱 Builds
    cursor.execute("SELECT title, due_date, completed FROM builds ORDER BY due_date ASC LIMIT 3")
    builds = cursor.fetchall()

    conn.close()

    # ---------------------
    # 🖥️ Render Dashboard
    print(Panel(logs_text, title="✅ Today's Logs", border_style="green"))

    print(Panel(
        f"🔥 Current Streak: [green]{streak}[/green] days\n🏆 Longest Streak: [blue]{longest}[/blue] days",
        title="🔥 Streak Tracker",
        border_style="cyan"
    ))

    if goals:
        goal_table = Table(title="🎯 Top Goals", show_header=True, header_style="bold magenta")
        goal_table.add_column("Goal")
        goal_table.add_column("Status")
        for goal, completed in goals:
            goal_table.add_row(goal, "✅" if completed else "⏳")
        console.print(goal_table)
    else:
        print("[yellow]No goals yet.[/yellow]")

    if builds:
        build_table = Table(title="🧱 Builds", show_header=True, header_style="bold blue")
        build_table.add_column("Title")
        build_table.add_column("Due In")
        build_table.add_column("Status")

        now = datetime.now()
        for title, due_date, completed in builds:
            due = datetime.fromisoformat(due_date)
            delta = (due - now).days
            due_in = f"{delta}d" if delta >= 0 else f"-{abs(delta)}d"
            status = "✅ Done" if completed else ("⏳ Active" if delta >= 0 else "❌ Overdue")
            build_table.add_row(title, due_in, status)

        console.print(build_table)
    else:
        print("[yellow]No active builds yet.[/yellow]")
