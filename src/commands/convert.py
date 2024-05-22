import os
from pathlib import Path
from typing import Annotated, Optional

import typer

from utils.convert import video_to_gif_ffmpeg, video_to_gif_moviepy
from utils.inquiries import should_continue, should_delete
from utils.providers import Provider
from utils.text import printc

app = typer.Typer()


@app.command(short_help='Converts a video to a gif.', name='convert')
def convert(
	input: Annotated[Path, typer.Argument(
		help = 'The input file path',
		exists = True, file_okay = True, dir_okay = False,
		writable = False, readable = True, resolve_path = True
	)],
	output: Annotated[Optional[Path], typer.Argument(
		help='The output file path.',
		writable = True, readable = False, resolve_path = True,
	)] = None,
	provider: Annotated[Provider, typer.Option(
		rich_help_panel = 'Optional Settings',
		help = 'The provider to use for the conversion.',
		case_sensitive = False
	)] = Provider.ffmpeg,
	start: Annotated[float, typer.Option(
		rich_help_panel = 'Optional Settings',
		help = 'At what time in seconds the gif should start.',
	)] = 0.0,
	end: Annotated[float, typer.Option(
		rich_help_panel = 'Optional Settings',
		help = 'At what time in seconds the gif should end.',
	)] = 0.0,
	fps: Annotated[int, typer.Option(
		rich_help_panel = 'Optional Settings',
		help = 'How many frames per second should the output have.'
	)] = 10
):
	"""
		Converts a video to a gif.

		Examples:



		$ python main.py video.mp4

		$ python main.py video.mp4 output.gif

		$ python main.py video.mp4 output.gif --provider ImageMagick --start 10 --end 20 --fps 15
	"""

	try:
		#? No output is given, inherit from input
		if output is None:
			output = Path(f'{input.stem}.gif')
			printc(f'&r[&c!&r]&e Output file not specified. Saving to &d{output.name}&e.')


		#! Output already exists, prompt to delete or not
		if output.exists():
			if not should_delete(output.name):
				return printc('&r[&c!&r]&c Aborted.')

			try:
				os.remove(output)
			except Exception as e:
				return printc(f'&r[&c!&r]&c Unable to delete the file &d{output.name}&c. {e}')


		#! Confirm the conversion
		if not should_continue(input.name, output.name):
			return printc('&r[&c!&r]&c Aborted.')


		#! Convert the video to a gif
		match provider:
			case Provider.ffmpeg:
				video_to_gif_ffmpeg(input, output, start, end, fps)
			case _:
				video_to_gif_moviepy(input, output, provider.name, start, end, fps)

	except KeyboardInterrupt:
		printc('&r[&c!&r]&c Aborted.')
	except Exception as e:
		printc(f'&r[&c!&r]&c {e}')