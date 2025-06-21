import sys
import click
import ftfy
from pathlib import Path
import requests
import json

from fetcherr.kemono_yaml_loader import load
from fetcherr.printf_info import print_formatted_info

KEMONO = load()

def download_creator_info_file():
    try:
        response_of_file = requests.get(KEMONO["kemono"]["url"] + KEMONO["kemono"]["requests"]["creators"], stream=True)
    except requests.exceptions.SSLError:
        click.echo(
            "SSLError occurred. This may be due to HTTPS interference or certificate issues.\n"
            "If you're accessing from a country that censors kemono.su (like mine), try using a VPN or 'zapret':\n"
            "https://github.com/bol-van/zapret"
        )
        sys.exit(1)

    if response_of_file.status_code == 200:
        data = response_of_file.json()

        for creator in data:
            if "name" in creator:
                creator["name"] = ftfy.fix_text(creator["name"])

        creators_file_download_path = Path(__file__).parent.parent / "creators.json"

        with open(creators_file_download_path, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


def get_info_of_creator(creator_name_or_id: str, printf: bool = False):
    creator_name_or_id = creator_name_or_id.replace('_', ' ')

    creators_file_path = Path(__file__).parent.parent / "creators.json"

    with open(creators_file_path, 'r') as f:
        creators = json.load(f)

    founded_creators = []

    for creator in creators:
        if creator.get("name") == creator_name_or_id or creator.get("id") == creator_name_or_id:

            founded_creators.append(creator)

    if printf:
        print_formatted_info(founded_creators)
        sys.exit(0)

    return founded_creators
