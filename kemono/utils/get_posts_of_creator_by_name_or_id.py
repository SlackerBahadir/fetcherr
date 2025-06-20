import sys
import click
import requests

from fetcherr.kemono_yaml_loader import load
from kemono.utils.creator_info import get_info_of_creator

KEMONO = load()

def get_posts(creator_id):
    creator_infos = get_info_of_creator(creator_id)

    full_url = (KEMONO["kemono"]["url"] + KEMONO["kemono"]["requests"]["creators_posts"]
                .replace("{service}", creator_infos["service"])
                .replace("{creator_id}", creator_infos["id"]))

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

        # COMPLETE THIS
