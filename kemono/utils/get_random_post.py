import subprocess
import sys
import click
import requests
import psutil
from pathlib import Path
import os

from fetcherr.kemono_yaml_loader import load
from fetcherr.printf_posts import print_formatted_post
from fetcherr.download_posts import download

KEMONO = load()

def get_terminal_emulator():
    parent = psutil.Process().parent()
    return parent.name()

def global_random_post():
    try:
        response = requests.get(KEMONO["kemono"]["url"] + KEMONO["kemono"]["requests"]["random_post"])
    except requests.exceptions.SSLError:
        click.echo(
            "SSLError occurred. This may be due to HTTPS interference or certificate issues.\n"
            "If you're accessing from a country that censors kemono.su (like mine), consider using a VPN or 'zapret':\n"
            "https://github.com/bol-van/zapret"
        )
        sys.exit(1)

    if response.status_code == 200:
        data = response.json()

        print_formatted_post(data)

        click.echo("Would you like to see the image in the terminal? (Currently only possible for the ‘kitty’ terminal)")

        choice = input("[y/n]: ")

        if choice.strip().lower() == "y":
            cache_dir = Path(__file__).parent.parent.parent / ".cache"

            if not os.path.exists(cache_dir):
                os.mkdir(cache_dir)

            image_paths = download(data, cache_dir.name, return_download_paths=True)

            # DEBUG TODO

            for path in image_paths:
                subprocess.run(["kitten", "+kitten", "icat", path])

