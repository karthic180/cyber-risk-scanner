import typer
from core.risk_calculator import calculate_risk

app = typer.Typer()

@app.command()
def scan(url: str):
    """Scan a URL for phishing detection"""
    result = calculate_risk(url)
    typer.echo(result)

if __name__ == "__main__":
    app()