import re

colors = {
    '0': '\x1b[0m\x1b[30m',
    '1': '\x1b[0m\x1b[1m\x1b[34m',
    '2': '\x1b[0m\x1b[1m\x1b[32m',
    '3': '\x1b[0m\x1b[1m\x1b[36m',
    '4': '\x1b[0m\x1b[1m\x1b[31m',
    '5': '\x1b[0m\x1b[1m\x1b[35m',
    '6': '\x1b[0m\x1b[1m\x1b[33m',
    '7': '\x1b[0m\x1b[1m\x1b[90m',
    '8': '\x1b[0m\x1b[90m',
    '9': '\x1b[0m\x1b[34m',
    'a': '\x1b[0m\x1b[32m',
    'b': '\x1b[0m\x1b[36m',
    'c': '\x1b[0m\x1b[31m',
    'd': '\x1b[0m\x1b[35m',
    'e': '\x1b[0m\x1b[33m',
    'f': '\x1b[0m\x1b[37m',
	'l': '\x1b[1m\x1b[37m',
    'r': '\x1b[0m'
}

def color_message(text: str) -> str:
    """
        Converts custom color codes to ansi color codes

        Color codes can be called using the & symbol or the § symbol

        Example: &1Hello §2World
    """
    return re.sub(
        r'&[0-9a-f|l|r]|§[0-9a-f|l|r]',
        lambda match: colors.get(match.group(0)[1], match.group(0)),
        text
    ) + '\x1b[0m'


def printc(text: str, clear_last_line: bool = False) -> None:
    """
        Parses text as a color message and prints it to the console
    """
    if clear_last_line:
        clear_line()

    print(color_message(text))


def clear_color_codes(text: str) -> str:
    """
        Removes all color codes from a string

        Color codes can be called using the & symbol or the § symbol

        Example: &1Hello §2World
    """
    return re.sub(r'&[0-9a-f|l|r]|§[0-9a-f|l|r]', '', text)


def cstring(text: str) -> str:
    """
	    Alias for color_message, stands for "colored string"
    """
    return color_message(text)

def clear_line():
    """
        Clears the last printed line, useful for rewriting prints and giving the illusion of updating text
    """
    print('\033[1A', end='\x1b[2K')