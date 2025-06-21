import click
import sys

def print_formatted_info(creators: list):
    if len(creators) == 0:
        click.echo("Creator not found.")
        sys.exit(1)

    for creator in creators:
        if creator:
            click.echo("-------------------------------------------/")
            for key, value in creator.items():
                click.echo(f"{key.capitalize()}: {value}")
            click.echo("-------------------------------------------\\")