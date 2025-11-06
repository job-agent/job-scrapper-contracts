"""
Core interfaces for the scrapper service architecture
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Callable, List, Optional

from .models import Job


class ScrapperServiceInterface(ABC):
    """
    Defines the contract for services that aggregate job postings from configured
    sources while enforcing a consistent API for downstream consumers.
    """

    @abstractmethod
    def scrape_jobs(
        self,
        min_salary: Optional[int],
        employment_location: Optional[str],
        posted_after: Optional[datetime],
        timeout: int,
        batch_size: int,
        on_jobs_batch: Optional[Callable[[List[Job], bool], None]],
    ) -> List[Job]:
        """
        Retrieve job postings from the configured providers, yielding batches until
        the pagination limit or posting date cutoff is reached.

        Args:
            min_salary: Minimum salary threshold applied to each listing.
            employment_location: Employment type or location filter.
            posted_after: Omit listings published before this timestamp; use None to include all.
            timeout: Request timeout in seconds for each provider interaction.
            batch_size: Maximum number of jobs fetched per pagination request.
            on_jobs_batch: Optional callback invoked with each batch and a flag indicating the final batch.

        Returns:
            Jobs gathered across all pages for the specified filters.
        """
        pass
