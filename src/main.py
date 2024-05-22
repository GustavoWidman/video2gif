import typer

from commands.convert import app as convert

app = typer.Typer(help="A CLI to convert videos into gifs.", name="video2gif")

app.registered_commands += convert.registered_commands

if __name__ == "__main__":
	app()