import typer
from cracktracker.db import get_db
from datetime import datetime

app = typer.Typer()


@app.command()
def log(entry: str = typer.Argument(..., help="What did you crack today?")):
    conn = get_db()
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    cursor.execute("INSERT INTO logs (content, timestamp) VALUES (?, ?)", (entry, now))
    conn.commit()
    conn.close()
    typer.echo(f"✅ Logged: {entry}")
