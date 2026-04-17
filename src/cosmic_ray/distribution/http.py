"""Cosmic Ray distributor that sends work requests over HTTP to workers.

This uses a list of URLs to workes, distributing work to them as they're available.

Enabling the distributor
========================

To use the http distributor, set ``cosmic-ray.distributor.name = "http"`` in your Cosmic Ray configuration, and
configure the list of worker URLs in ``cosmic-ray.distributor.http.worker-urls``:

.. code-block:: toml

    [cosmic-ray.distributor]
    name = "http"

    [cosmic-ray.distributor.http]
    worker-urls = ['http://localhost:9876', 'http://localhost:9877']
"""

import asyncio
import logging
from pathlib import Path

import aiohttp
from aiohttp import web

from cosmic_ray.distribution.distributor import Distributor
from cosmic_ray.mutating import mutate_and_test
from cosmic_ray.work_item import MutationSpec, WorkItem, WorkResult, WorkerOutcome

log = logging.getLogger(__name__)


class HttpDistributor(Distributor):
    """The http distributor.

    This forwards mutate-and-test requests to HTTP servers which do the actual work and
    return the results.
    """

    def __call__(self, *args, **kwargs):
        # TODO: We still have the issue that `pending_work` is a running query on the database. Will `on_task_complete`
        # - which writes results to the database - be able to complete, or will it be blocked? Do we have to copy the
        # pending work as we used to do?

        # TODO: Will there be an event loop? Where should we ensure that there is?
        asyncio.get_event_loop().run_until_complete(self._process(*args, **kwargs))

    async def _process(self, pending_work, test_command, timeout, config, on_task_complete):
        pass


async def send_request(url, work_item: WorkItem, test_command, timeout):
    """Sends a mutate-and-test request to a worker.

    Args:
        url: The URL of the worker.
        work_item: The `WorkItem` representing the work to be done.
        test_command: The command that the worker should use to run the tests.
        timeout: The maximum number of seconds to spend running the test.

    Returns: A `WorkResult`.
    """
    pass


async def handle_mutate_and_test(request):
    """HTTP endpoint handler for requests to mutate-and-test."""
    pass


def run_worker(port=None, path=None):
    """Run the worker HTTP server.

    You must specify either `port` or `path`, but not both.

    Args:
        port: The TCP port on which to listen.
        path: Path to Unix domain socket on which to listen.
    """
    pass
