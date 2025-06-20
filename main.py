import click
import sys
from kemono.utils.creator_info import download_creator_info_file, print_formatted_info
from kemono.utils.get_posts_of_creator_by_name_or_id import print_formatted_post

__version__ = "0.1.0"

@click.command(help="Fetcherr: Kemono scraper CLI")
@click.version_option(__version__, prog_name="fetcherr")
@click.option('--info', is_flag=True, help="Get detailed info of a creator.")
@click.option('--refresh', is_flag=True, help="Refresh creators.json file.")
@click.option('--getposts', is_flag=True, help="Get posts from the selected creator. Mostly meaningless when not used with '--installall'. Defaultly fetches every post.")
@click.option('--creator', '-c', help="Set creator with specifying name or ID of creator to be used with '--info', '--installall' and '--getallposts'.")
@click.option('--installall', is_flag=True, help="Download all posts of selected creator's posts.")
@click.option('--number', help="Number of post that will fetched. Use with only '--getposts'.", type=int)
def parser(info, refresh, getposts, creator, installall, number, c = None):
    if refresh:
        download_creator_info_file()

    if info:
        print_formatted_info(creator)

    if getposts:
        print_formatted_post(creator, number=number)

    if getposts and installall:
        pass

if __name__ == '__main__':
    if len(sys.argv) == 1:
        click.echo(parser.get_help(click.Context(parser)))
        sys.exit(0)

    parser()
