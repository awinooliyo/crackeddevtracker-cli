import typer
from cracktracker.commands import (
        add, log, stats, init, goals,
        build, streaks, dashboard
)

app = typer.Typer()
app.add_typer(add.app, name="add")
app.add_typer(log.app, name="log")
app.add_typer(stats.app, name="stats")
app.add_typer(init.app, name="init")
app.add_typer(goals.app, name="goals")
app.add_typer(build.app, name="build")
app.add_typer(streaks.app, name="streaks")
app.add_typer(dashboard.app, name="dashboard")

if __name__ == "__main__":
    app()
