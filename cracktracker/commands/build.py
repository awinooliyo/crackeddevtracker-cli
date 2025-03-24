import typer
from datetime import datetime, timedelta
from cracktracker.db import get_db
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

@app.command()
def new(title: str, days: int = typer.Option(3, help="Days to complete the build")):
    """Start a new build challenge"""
    conn = get_db()
    cursor = conn.cursor()
    now = datetime.now()
    due = now + timedelta(days=days)
    cursor.execute("INSERT INTO builds (title, created, due_date, completed) VALUES (?, ?, ?, ?)",
                   (title, now.isoformat(), due.isoformat(), 0))
    conn.commit()
    conn.close()
    console.print(f"[bold green]🧱 Build added:[/bold green] {title} (due in {days} days)")

@app.command()
def list():
    """Show your current builds"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, created, due_date, completed FROM builds ORDER BY due_date ASC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print("[yellow]No builds yet. Add one with:[/yellow] crack build new \"Your Build\"")
        return

    table = Table(title="🧱 Active Builds")
    table.add_column("ID", style="dim")
    table.add_column("Title", style="bold")
    table.add_column("Due In", style="green")
    table.add_column("Status", style="white")

    now = datetime.now()

    for id, title, created, due_date, completed in rows:
        due_dt = datetime.fromisoformat(due_date)
        delta = due_dt - now
        status = "✅ Done" if completed else ("⏳ In Progress" if delta.days >= 0 else "❌ Overdue")
        due_text = f"{delta.days}d" if delta.days >= 0 else f"-{abs(delta.days)}d"
        table.add_row(str(id), title, due_text, status)

    console.print(table)
