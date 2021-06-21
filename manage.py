#!/usr/bin/env python3
# vim: ft=python

import click

from server_manager.config import cli as config_cli
from server_manager.jars.cli import cli as jars_cli
from server_manager.synchronize.cli import cli as synchronize_cli


@click.group()
def cli():
    pass


cli.add_command(config_cli, name="config")
cli.add_command(synchronize_cli, name="synchronize")
cli.add_command(jars_cli, name="jars")

if __name__ == "__main__":
    cli()
