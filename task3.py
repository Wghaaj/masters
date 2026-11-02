import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def show_directory(path, level=0):

    """
    Task 3 - Directory Structure

    This script displays the files and folders inside a given directory.

    It uses sys.argv to get the directory path, pathlib to work with files
    and folders, and colorama to display them in different colours.

    The show_directory() function goes through folders recursively and
    prints their contents. The script also checks if the path exists
    and handles errors.
    """
    try:
        items = sorted(path.iterdir(), key=lambda item: (item.is_file(), item.name.lower()))

        for item in items:
            indent = "    " * level

            if item.is_dir():
                print(indent + Fore.BLUE + "📂 " + item.name + Style.RESET_ALL)
                show_directory(item, level + 1)

            else:
                print(indent + Fore.GREEN + "📄 " + item.name + Style.RESET_ALL)

    except PermissionError:
        print(Fore.RED + "Error: Access denied to " + str(path))


if len(sys.argv) < 2:
    print(Fore.RED + "Error: Please provide a directory path.")

else:
    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Error: Path does not exist.")

    elif not path.is_dir():
        print(Fore.RED + "Error: Path is not a directory.")

    else:
        print(Fore.BLUE + "📂 " + path.name)
        show_directory(path)
