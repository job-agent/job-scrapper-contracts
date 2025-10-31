"""
Core interfaces for the scrapper service architecture
"""

from abc import ABC, abstractmethod
from typing import List

from .models import Job, JobDict


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
        page: int = 1,
        timeout: int = 30
    ) -> List[Job]:
        """
        Scrape jobs from configured sources.

        Args:
            salary: Minimum salary filter (default: 4000)
            employment: Employment type filter (default: "remote")
            page: Page number for pagination (default: 1)
            timeout: Request timeout in seconds (default: 30)

        Returns:
            List of Job objects
        """
        pass

    @abstractmethod
    def scrape_jobs_as_dicts(
        self,
        salary: int = 4000,
        employment: str = "remote",
        page: int = 1,
        timeout: int = 30
    ) -> List[JobDict]:
        """
        Scrape jobs and return as dictionaries.

        Args:
            salary: Minimum salary filter (default: 4000)
            employment: Employment type filter (default: "remote")
            page: Page number for pagination (default: 1)
            timeout: Request timeout in seconds (default: 30)

        Returns:
            List of job dictionaries
        """
        pass