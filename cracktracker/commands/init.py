import typer
from cracktracker.db import init_db
from rich import print

app = typer.Typer()


@app.command()
def db():
    """Initialize the database with tables"""
    init_db()
    print("✅ Database initialized.")
