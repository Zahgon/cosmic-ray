"""Tool for creating badge."""

import os
from logging import getLogger

import click
from anybadge import Badge

from cosmic_ray.config import load_config
from cosmic_ray.tools.survival_rate import survival_rate
from cosmic_ray.work_db import WorkDB, use_db

log = getLogger()


@click.command()
@click.argument("config_file", type=click.Path(exists=True, dir_okay=False, readable=True))
@click.argument("badge_file", type=click.Path(dir_okay=False, writable=True))
@click.argument("session_file", type=click.Path(exists=True, dir_okay=False, readable=True))
def generate_badge(config_file, badge_file, session_file):
    """Generate badge file."""
    pass
