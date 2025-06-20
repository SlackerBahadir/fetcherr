import click
import sys
from kemono.utils.creator_info import download_creator_info_file, print_formatted
from kemono.utils.get_posts_of_creator_by_name_or_id import get_posts

@click.command(help="Fetcherr: Kemono scraper CLI")
@click.option('--info', is_flag=True, help="Get detailed info of a creator.")
@click.option('--refresh', is_flag=True, help="Refresh creators.json file.")
@click.option('--getposts', '-g', help="Get posts from the selected creator.")
@click.option('--creator', help="Set creator name or ID to be used with --info or --installall.")
@click.option('--installall', is_flag=True, help="Download all posts of selected creator.")
def parser(info, refresh, getposts, creator, installall):
    if refresh:
        download_creator_info_file()

    if info:
        print_formatted(creator)

    if getposts:
        get_posts() # TODO

    if installall:
        click.echo("Install-all is not implemented yet.")  # TODO

if __name__ == '__main__':
    if len(sys.argv) == 1:
        click.echo(parser.get_help(click.Context(parser)))
        sys.exit(0)

    parser()
