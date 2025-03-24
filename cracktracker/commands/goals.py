import typer
from cracktracker.db import get_db
from datetime import datetime
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

@app.command()
def add(goal: str):
    """Add a long-term dev goal"""
    conn = get_db()
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    cursor.execute("INSERT INTO goals (goal, completed, timestamp) VALUES (?, ?, ?)", (goal, 0, now))
    conn.commit()
    conn.close()
    console.print(f"[green]✅ Goal added:[/green] {goal}")

@app.command()
def list():
    """List your current dev goals"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, goal, completed FROM goals ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print("[yellow]No goals yet. Add one with:[/yellow] crack goals add \"Your Goal\"")
        return

    table = Table(title="🎯 Dev Goals")
    table.add_column("ID", style="dim")
    table.add_column("Goal", style="white")
    table.add_column("Status", style="green")

    for id, goal, completed in rows:
        status = "✅ Done" if completed else "⏳ In Progress"
        table.add_row(str(id), goal, status)

    console.print(table)

@app.command()
def done(goal_id: int):
    """Mark a goal as complete"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE goals SET completed = 1 WHERE id = ?", (goal_id,))
    conn.commit()
    conn.close()
    console.print(f"[green]🎯 Goal #{goal_id} marked as complete.[/green]")
