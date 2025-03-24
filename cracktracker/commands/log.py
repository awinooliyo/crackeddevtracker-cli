import typer
from cracktracker.db import get_db
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

@app.command()
def all():
    """Show all cracked logs"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, content FROM logs ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print("[yellow]No logs found.[/yellow]")
        return

    table = Table(title="🔥 Crack Logs")
    table.add_column("Timestamp", style="cyan")
    table.add_column("Log Entry", style="white")

    for timestamp, content in rows:
        table.add_row(timestamp[:19], content)

    console.print(table)
