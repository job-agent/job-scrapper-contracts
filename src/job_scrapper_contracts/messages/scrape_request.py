"""Message contract for scrape jobs request."""

from typing import Optional, TypedDict


class ScrapeJobsRequest(TypedDict, total=False):
    """Request message for scraping jobs.

    Attributes:
        salary: Minimum salary requirement
        employment: Employment type (e.g., "remote", "full-time", "part-time")
        posted_after: Only include jobs posted after this date (ISO format string)
        timeout: Request timeout in seconds
    """

    salary: int
    employment: str
    posted_after: Optional[str]
    timeout: int
