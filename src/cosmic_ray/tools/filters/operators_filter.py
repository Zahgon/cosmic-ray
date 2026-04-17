"""An filter that removes operators based on regular expressions."""

import logging
import re
import sys
from argparse import ArgumentParser, Namespace

from cosmic_ray.config import load_config
from cosmic_ray.tools.filters.filter_app import FilterApp
from cosmic_ray.work_db import WorkDB
from cosmic_ray.work_item import WorkResult, WorkerOutcome

log = logging.getLogger()


class OperatorsFilter(FilterApp):
    "Implemenents the operators-filter."

    def description(self):
        return __doc__

    def _skip_filtered(self, work_db, exclude_operators):
        pass

    def filter(self, work_db: WorkDB, args: Namespace):
        """Mark as skipped all work item with filtered operator"""
        pass

    def add_args(self, parser: ArgumentParser):
        parser.add_argument("config", help="Config file to use")


def main(argv=None):
    """Run the operators-filter with the specified command line arguments."""
    return OperatorsFilter().main(argv)


if __name__ == "__main__":
    sys.exit(main())
