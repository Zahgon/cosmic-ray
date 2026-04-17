"""A filter that uses git to determine when specific files/lines
should be skipped.
"""

import logging
import re
import subprocess
import sys
from argparse import Namespace
from collections import defaultdict
from pathlib import Path

from cosmic_ray.config import ConfigDict, load_config
from cosmic_ray.tools.filters.filter_app import FilterApp
from cosmic_ray.work_db import WorkDB
from cosmic_ray.work_item import WorkResult, WorkerOutcome

log = logging.getLogger()


class GitFilter(FilterApp):
    """Implements the git filter."""

    def description(self):
        return __doc__

    def _git_news(self, branch):
        """Get the set of new lines by file"""
        pass

    def _skip_filtered(self, work_db, branch):
        pass

    def filter(self, work_db: WorkDB, args: Namespace):
        """Mark as skipped all work item that is not new"""
        pass

    def add_args(self, parser):
        parser.add_argument("--config", help="Config file to use")


def main(argv=None):
    """Run the operators-filter with the specified command line arguments."""
    return GitFilter().main(argv)


if __name__ == "__main__":
    sys.exit(main())
