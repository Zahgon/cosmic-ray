"""A filter that uses "# pragma: no mutate" to determine when specific mutations
should be skipped.
"""

import logging
import re
import sys
from functools import lru_cache

from cosmic_ray.tools.filters.filter_app import FilterApp
from cosmic_ray.work_item import WorkResult, WorkerOutcome

log = logging.getLogger()


class PragmaNoMutateFilter(FilterApp):
    """Implements the pragma-no-mutate filter."""

    def description(self):
        return __doc__

    def filter(self, work_db, _args):
        """Mark lines with "# pragma: no mutate" as SKIPPED

        For all work_item in db, if the LAST line of the working zone is marked
        with "# pragma: no mutate", This work_item will be skipped.
        """
        pass


def main(argv=None):
    """Run pragma-no-mutate filter with specified command line arguments."""
    return PragmaNoMutateFilter().main(argv)


if __name__ == "__main__":
    sys.exit(main())
