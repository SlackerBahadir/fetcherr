import sys
import click
import requests
import html2text as h2t

from fetcherr.kemono_yaml_loader import load
from kemono.utils.creator_info import get_info_of_creator

KEMONO = load()


def get_posts(creator_id_or_name: str, service: str = None, number: int = None):
    if number and number % 50 == 0:
        click.echo("You must write an offset in multiples of 50.")

    creator_infos = get_info_of_creator(creator_id_or_name)

    if len(creator_infos) == 0:
        click.echo("Creator not found.")
        sys.exit(1)

    if service is not None:
        full_url = (KEMONO["kemono"]["url"] + KEMONO["kemono"]["requests"]["creators_posts"]
                    .replace("{service}", service)
                    .replace("{creator_id}", creator_infos["id"])
                    .replace("{number}", number))
    else:
        full_url = (KEMONO["kemono"]["url"] + KEMONO["kemono"]["requests"]["creators_posts"]
                    .replace("{service}", creator_infos[0]["service"])
                    .replace("{creator_id}", creator_infos[0]["id"])
                    .replace("{number}", str(number)))
        
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

        if number is not None:
            return data[:number]
        return data

    click.echo(response.status_code)

    return None


def print_formatted_post(creator_id_or_name: str, service: str = None, number: int = None):
    posts = get_posts(creator_id_or_name, service, number)

    if len(posts) == 0 or posts:
        click.echo("Creator has no posts.")

    for post in posts:
        content = h2t.html2text(post.get('content'))
        click.echo("-------------------------------------------/")
        click.echo(
            f"Id: {post.get('id')}\n"
            f"Creator Id: {post.get('user')}\n"
            f"Service: {post.get('service')}\n"
            f"Title of Post: {post.get('title')}\n"
            f"Description: {content}"
            f"Attachments: {post.get('attachments')}"
        )
        click.echo("-------------------------------------------\\")
