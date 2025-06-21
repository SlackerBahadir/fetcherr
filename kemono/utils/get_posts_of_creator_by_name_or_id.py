import sys
import click
import requests
import html2text as h2t

from fetcherr.kemono_yaml_loader import load
from fetcherr.printf_posts import print_formatted_post

from kemono.utils.creator_info import get_info_of_creator

KEMONO = load()


def get_posts(creator_id_or_name: str, service: str = None, offset: int = None, printf: bool = False):
    if offset is not None and offset % 50 != 0:
        click.echo("Offset value must be in multiples of 50.")
        sys.exit(1)

    creator_infos = get_info_of_creator(creator_id_or_name)

    if len(creator_infos) == 0:
        click.echo("Creator not found.")
        sys.exit(1)

    if service is not None:
        full_url = (KEMONO["kemono"]["url"] + KEMONO["kemono"]["requests"]["creators_posts"]
                    .replace("{service}", service)
                    .replace("{creator_id}", creator_infos["id"])
                    .replace("{number}", offset))
    else:
        full_url = (KEMONO["kemono"]["url"] + KEMONO["kemono"]["requests"]["creators_posts"]
                    .replace("{service}", creator_infos[0]["service"])
                    .replace("{creator_id}", creator_infos[0]["id"])
                    .replace("{number}", str(offset)))
        
    try:
        response = requests.get(full_url)
    except requests.exceptions.SSLError:
        click.echo(
            "SSLError occurred. This may be due to HTTPS interference or certificate issues.\n"
            "If you're accessing from a country that censors kemono.su (like mine), consider using a VPN or 'zapret':\n"
            "https://github.com/bol-van/zapret"
        )
        sys.exit(1)

    if response.status_code == 200:
        data = response.json()

        if printf:
            print_formatted_post(data)
            sys.exit(0)

        return data

    return None
