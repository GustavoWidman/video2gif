from pathlib import Path
from typing import Literal

import ffmpeg
import proglog
import yaspin
from moviepy.editor import VideoFileClip

from utils.text import cstring, printc

custom_spinner = yaspin.Spinner([
	cstring("[&e⠋&r]"), cstring("[&e⠙&r]"), cstring("[&e⠹&r]"),
  	cstring("[&e⠸&r]"), cstring("[&e⠼&r]"), cstring("[&e⠴&r]"),
	cstring("[&e⠦&r]"), cstring("[&e⠧&r]"), cstring("[&e⠇&r]"),
	cstring("[&e⠏&r]")], 80) # type: ignore


def video_to_gif_ffmpeg(
    input_path: Path,
    output_path: Path,
    start: float = 0.0,
    end: float = 0.0,
    fps: int = 10
):
    """
        Converts a video to a gif using ffmpeg-python (fastest method)

        Args:
            input_path (Path): The path to the video file
            output_path (Path): The path to save the gif
            start (float, optional): At what time in seconds the gif should start. Defaults to 0.0.
            end (float, optional): At what time in seconds the gif should end. Defaults to 0.0, in which case the whole video is converted.
            fps (int, optional): How many frames per second should the output have. Defaults to 10.
    """
    spinner_text = "&eConverting video to gif using &dffmpeg&e"

    if start != 0.0:
        spinner_text += f", starting at &d{start}&e seconds"

    if end != 0.0:
        spinner_text += f", ending at &d{end}&e seconds"

    spinner_text += f", with &d{fps}&e fps..."

    with yaspin.yaspin(custom_spinner, text = cstring(spinner_text)) as spinner:
        try:
            input_params = { 'ss': start } if start != 0.0 else {}

            output_params = { 'vf': f'fps={fps}' }

            if end != 0.0:
                output_params['t'] = str(end - start)

            (ffmpeg
                .input(str(input_path), **input_params)
                .output(str(output_path), **output_params)
            ).global_args('-loglevel', 'error').run()


            spinner.text = cstring(f'&aConversion complete! &d{output_path.name}&a has been saved.')
            spinner.ok(cstring("&r[&a✔&r]"))
        except Exception as e:
            spinner.text = cstring(f'&cError while converting the video to gif. {e}')
            spinner.fail(cstring(f"&r[&c!&r]&c {e}"))


def video_to_gif_moviepy(
    input_path: Path,
    output_path: Path,
    provider: Literal['imageio', 'ImageMagick'],
    start: float = 0.0,
    end: float = 0.0,
    fps: int = 10,
):
    """
        Converts a video to a gif using moviepy

        Args:
            input_path (Path): The path to the video file
            output_path (Path): The path to save the gif
            provider (str): The provider to use for the conversion. Has to be one of 'imageio' or 'ImageMagick'
            start (float, optional): At what time in seconds the gif should start. Defaults to 0.0.
            end (float, optional): At what time in seconds the gif should end. Defaults to 0.0, in which case the whole video is converted.
            fps (int, optional): How many frames per second should the output have. Defaults to 10.
    """
    text = f"&r[&e?&r]&e Converting video to gif using &d{provider}&e"

    if start != 0.0:
        text += f", starting at &d{start}&e seconds"

    if end != 0.0:
        text += f", ending at &d{end}&e seconds"

    text += f", with &d{fps}&e fps..."

    printc(text)

    try:
        clip = VideoFileClip(str(input_path))

        if start != 0.0 or end != 0.0:
            clip = clip.subclip(start, end)

        clip.write_gif(
            str(output_path), fps = fps, logger = proglog.TqdmProgressBarLogger(print_messages=False),
            verbose = False, program = provider
        )
    except Exception as e:
        return printc(
            f"&r[&c!&r]&c Error while converting the video to gif. {e}",
            clear_last_line = True
        )

    printc(
        f"&r[&a✔&r]&a Conversion complete! &d{output_path.name}&a has been saved.",
        clear_last_line = True
    )