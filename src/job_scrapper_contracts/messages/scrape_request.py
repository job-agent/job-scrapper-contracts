"""Message contract for scrape jobs request."""

from typing import TypedDict

from job_scrapper_contracts.scrape_filter import ScrapeJobsFilter


class ScrapeJobsRequest(TypedDict, total=False):
    """Request message for scraping jobs.

    Attributes:
        filter: Filtering options for the request
        timeout: Request timeout in seconds
        batch_size: Optional batch size for streaming callbacks
    """

    filter: ScrapeJobsFilter
    timeout: int
    batch_size: int
