"""
Core interfaces for the scrapper service architecture
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

from .models import Job


class ScrapperServiceInterface(ABC):
    """
    Protocol defining the interface for job scrapper service implementations.

    This interface ensures that any scrapper service provides a consistent API
    for scraping jobs and returning them in various formats.
    """

    @abstractmethod
    def scrape_jobs(
        self,
        salary: int = 4000,
        employment: str = "remote",
        posted_after: Optional[datetime] = None,
        timeout: int = 30,
    ) -> List[Job]:
        """
        Scrape jobs from configured sources.

        Automatically paginates through all pages until reaching the date cutoff.

        Args:
            salary: Minimum salary filter (default: 4000)
            employment: Employment type filter (default: "remote")
            posted_after: Only return jobs posted after this datetime (default: None, returns all jobs)
            timeout: Request timeout in seconds (default: 30)

        Returns:
            List of Job objects
        """
        pass
