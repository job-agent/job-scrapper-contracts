"""Filters for job scraping requests."""

from typing import Optional, TypedDict


class ScrapeJobsFilter(TypedDict, total=False):
    """Filters for job scraping requests.

    Attributes:
        min_salary: Minimum salary requirement
        employment_location: Employment type or location (e.g., "remote", "full-time", "on-site")
        posted_after: Only include jobs posted after this date (ISO format string)
    """

    min_salary: Optional[int]
    employment_location: Optional[str]
    posted_after: Optional[str]
