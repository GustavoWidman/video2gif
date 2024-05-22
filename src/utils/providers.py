from enum import Enum


class Provider(str, Enum):
	"""
		List of available providers for video to gif conversion
	"""
	ffmpeg = "ffmpeg"
	imageio = "imageio"
	ImageMagick = "ImageMagick"