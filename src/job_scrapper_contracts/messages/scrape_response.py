"""Message contract for scrape jobs response."""

from typing import List, Optional, TypedDict

from job_scrapper_contracts.models.job import JobDict


class ScrapeJobsResponse(TypedDict, total=False):
    """Response message for scraping jobs.

    Attributes:
        jobs: List of scraped jobs as JobDict objects
        success: Whether the scraping operation was successful
        error: Error message if the operation failed
        jobs_count: Number of jobs scraped
        is_complete: Whether this is the final response (True) or a page result (False)
        page_number: The page number for this batch of jobs (for page responses)
        total_jobs: Total number of jobs scraped across all pages (only in final response)
    """

    jobs: List[JobDict]
    success: bool
    error: Optional[str]
    jobs_count: int
    is_complete: bool
    page_number: Optional[int]
    total_jobs: Optional[int]
