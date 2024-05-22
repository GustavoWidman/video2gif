# video2gif

## Description

This is a overengineered python CLI that uses `rich` and `typer` to make itself fancier than it should be.  It converts any video file to a gif file and allows you to set the start and end time of the video, aswell as the fps of the gif and what converter you want to use (available options are `ffmpeg`, `imageio` and `ImageMagick`, the last two of which use `moviepy` which ends up making them a slower option).

## Dependencies

The following dependencies listed here are python dependencies and the ones I used to develop the script. Note that if you run the `build.sh` script to build your own executable or download the one I built on the releases page, you won't need to install any of these.

- [rich](https://pypi.org/project/rich/) v13.7.1
- [typer](https://pypi.org/project/typer/) v0.12.3
- [inquirer](https://pypi.org/project/inquirer/) v3.2.4
- [yaspin](https://pypi.org/project/yaspin/) v3.0.2
- [moviepy](https://pypi.org/project/moviepy/) v1.0.3
- [ffmpeg-python](https://pypi.org/project/ffmpeg-python/) v0.2.0

These next dependencies are not python dependencies but system dependencies that you will need to install in order to use some of the provided converters.

- [ffmpeg](https://ffmpeg.org/)
- [ImageMagick](https://imagemagick.org/index.php)

Please consult your package manager's documentation on how to install these packages. If you are like me and you use Arch Linux (btw), you can install them with the following command:

```bash
sudo pacman -S ffmpeg imagemagick
```

Note: I'm pretty sure these come default with something on arch btw because i already had them installed but make sure they are installed nonetheless.

## Installation

Download the executable from the [releases page](https://github.com/GustavoWidman/video2gif/releases/) and add it to your PATH or just throw it in `/usr/local/bin` if you feel like it.

## Manual Build

If you want to build the executable yourself, you can run the `build.sh` script. This script will create a virtual environment, install the dependencies and then use `nuitka` to compile the script into an executable. You can run the script with the following command:

```bash
chmod +x build.sh # make sure the script is executable before running!
./build.sh
```

Note that the script takes a bit because `nuitka` is kind of slow.

## Usage

After installed and added to your PATH, you can check the help message by running the following command:

```bash
$ video2gif --help

 Usage: video2gif [OPTIONS] INPUT [OUTPUT]

 Converts a video to a gif.
 Examples:

 $ python main.py video.mp4
 $ python main.py video.mp4 output.gif
 $ python main.py video.mp4 output.gif --provider ImageMagick --start 10 --end 20 --fps 15

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    input       FILE      The input file path [default: None] [required]                                                    │
│      output      [OUTPUT]  The output file path. [default: None]                                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                      │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.               │
│ --help                        Show this message and exit.                                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Optional Settings ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --provider        [ffmpeg|imageio|ImageMagick]  The provider to use for the conversion. [default: ffmpeg]                    │
│ --start           FLOAT                         At what time in seconds the gif should start. [default: 0.0]                 │
│ --end             FLOAT                         At what time in seconds the gif should end. [default: 0.0]                   │
│ --fps             INTEGER                       How many frames per second should the output have. [default: 10]             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

This will show you the help message with all the available options. You can also run the script without any arguments and it will prompt you for the required arguments.

## Examples

Here are some examples of how you can use the script:


```bash
# Convert the `video.mp4` file to a gif called `video.gif` with the default settings (starts at 0 seconds, ends at the end of the video, 10 fps and uses `ffmpeg` as the converter).

$ video2gif video.mp4
```

```bash
# Convert the `video.mp4` file to a gif called `output.gif` with the default settings (starts at 0 seconds, ends at the end of the video, 10 fps and uses `ffmpeg` as the converter).

$ video2gif video.mp4 output.gif
```

```bash
# Convert the `video.mp4` file to a gif called `output.gif` with the following settings (starts at 10 seconds, ends at 20 seconds, 15 fps and uses `ImageMagick` as the converter).

$ video2gif video.mp4 output.gif --provider ImageMagick --start 10 --end 20 --fps 15
```

## License

This project is licensed under the CC0 1.0 Universal License - see the [LICENSE](LICENSE) file for details.
