import click
import requests
import os
import sys

from fetcherr.kemono_yaml_loader import load

KEMONO = load()

def download(posts: dict, path: str):
    for post in posts:
        files = post.get("attachments")
        for url in KEMONO["kemono"]["image_urls"].values():
            for file in files.copy():
                click.echo(url)

                file_name = file.get("name")
                download_path = os.path.join(path, file_name)
                
                if os.path.exists(download_path):
                    click.echo(f"{file_name} named file exists. Passing...")
                    files.remove(file)
                    continue
                
                try:
                    response = requests.get(url + file.get("path"))
                except requests.exceptions.SSLError:
                    click.echo(
                        "SSLError occurred. This may be due to HTTPS interference or certificate issues.\n"
                        "If you're accessing from a country that censors kemono.su (like mine), consider using a VPN or 'zapret':\n"
                        "https://github.com/bol-van/zapret"
                    )
                    sys.exit(1)

                if response.status_code == 200:
                    with open(download_path, 'wb') as f:
                        f.write(response.content)

                    click.echo(f"Installed {file_name} successfully.")
                    files.remove(file)
                else:
                    continue
