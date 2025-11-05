"""Message contract for scrape jobs response."""

from typing import List, Optional, TypedDict

from job_scrapper_contracts.models.job import JobDict


class ScrapeJobsResponse(TypedDict):
    """Response message for scraping jobs.

    Attributes:
        jobs: List of scraped jobs as JobDict objects
        success: Whether the scraping operation was successful
        error: Error message if the operation failed
        jobs_count: Number of jobs scraped
    """

    jobs: List[JobDict]
    success: bool
    error: Optional[str]
    jobs_count: int
