"A tool for generating HTML reports."

import datetime
from itertools import chain

import click
from yattag import Doc

from cosmic_ray.tools.survival_rate import kills_count, survival_rate
from cosmic_ray.work_db import WorkDB, use_db
from cosmic_ray.work_item import TestOutcome


@click.command()
@click.option("--only-completed/--not-only-completed", default=False)
@click.option("--skip-success/--include-success", default=False)
@click.option("--hide-skipped/--show-skipped", default=False)
@click.argument("session-file", type=click.Path(dir_okay=False, readable=True, exists=True))
def report_html(only_completed, skip_success, hide_skipped, session_file):
    """Print an HTML formatted report of test results."""
    pass


# TODO: Redo this with jinja?


def _generate_html_report(db, only_completed, skip_success, hide_skipped):
    # pylint: disable=too-many-statements
    pass


def _generate_job_list(doc, db, skip_success, hide_skipped):
    pass


# flake8: noqa: C901
def _generate_work_item_card(doc, index, work_item, result, skip_success, hide_skipped):
    pass


def _generate_summary(doc, db):
    pass


def pycharm_url(filename, line_number):
    "Get a URL for opening a file in Pycharm."
    pass
