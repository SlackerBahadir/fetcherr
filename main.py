import os
import click
import sys

from kemono.utils.creator_info import download_creator_info_file, get_info_of_creator
from kemono.utils.get_posts_of_creator_by_name_or_id import get_posts
from fetcherr.download_posts import download
from kemono.utils.get_random_post import global_random_post

__version__ = "0.1.0"

@click.command(help="Fetcherr: Kemono scraper CLI")
@click.version_option(__version__, prog_name="fetcherr")
@click.option('--info', is_flag=True, help="Get detailed info of a creator.")
@click.option('--refresh', is_flag=True, help="Refresh creators.json file.")
@click.option('--getposts', '-g', is_flag=True, help="Get posts from the selected creator. Mostly meaningless when not used with '--installall'. Defaultly fetches every post.")
@click.option('--creator', '-c', help="Set creator with specifying name or ID of creator to be used with '--info', '--installall' and '--getallposts'.")
@click.option('--install', is_flag=True, help="Download all posts of selected creator's posts.")
@click.option('--offset', '-n', help="Offset of post that will fetched. Use with only '--getposts'.", type=int)
@click.option('--service', help="Selecting creators service.")
@click.option('--path', '-p', help="Selects path for downloading images.")
@click.option('--random', is_flag=True, help="Randomly picks a post and shows details. Optionally shows the image on the terminal.")
def parser(info, refresh, getposts, creator, install, service, path, offset, random):
    creators_file_path = os.path.join(__file__, "kemono", "creators.json")

    if refresh:
        download_creator_info_file()

    if info:
        get_posts(creator, printf=True)

    if getposts and not install:
        get_posts(creator, service=service, offset=offset, printf=True)

    if getposts and install:
        posts = get_posts(creator, service=service, offset=offset)
        download(posts, path)

    if random:
        global_random_post()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        click.echo(parser.get_help(click.Context(parser)))
        sys.exit(0)

    parser()
