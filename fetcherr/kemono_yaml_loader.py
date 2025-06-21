import click
from pathlib import Path
import yaml
import sys

KEMONO_YAML = Path(__file__).parent.parent / "kemono" / "kemono.yml"

def load():
    with open(KEMONO_YAML, 'r') as f:
        try:
            kemono = yaml.safe_load(f)

            return kemono
        except yaml.YAMLError as e:
            click.echo("There is a problem with your ‘kemono.yml’ file. It shouldn't have happened.\n"
                       "If you tried to adjust it yourself (which is probably what happened) please restore it.")
            sys.exit(1)
        except FileNotFoundError:
            click.echo("The file ‘kemono.yml’ was not found. Please make sure you have downloaded the repo correctly.")
            sys.exit(1)
