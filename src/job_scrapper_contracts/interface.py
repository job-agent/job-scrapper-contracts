"""
Abstract interface for job scrapper services

This interface defines the contract that all job scrapper implementations must follow.
"""

from abc import ABC, abstractmethod
from typing import List

from .models import Job, JobDict


class JobScrapperInterface(ABC):
    """
    Abstract base class for job scrapping services.

    All job scrapper implementations (Djinni, LinkedIn, etc.) should implement this interface
    to ensure consistent behavior across different scrapping sources.
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
        Scrape jobs and return Job objects.

        Args:
            salary: Minimum salary filter (default: 4000)
            employment: Employment type filter (default: "remote")
            page: Page number for pagination (default: 1)
            timeout: Request timeout in seconds (default: 30)

        Returns:
            List of Job objects

        Raises:
            Exception: Implementation-specific exceptions for request/parsing failures
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
        Scrape jobs and return as dictionaries instead of Job objects.

        Args:
            salary: Minimum salary filter (default: 4000)
            employment: Employment type filter (default: "remote")
            page: Page number for pagination (default: 1)
            timeout: Request timeout in seconds (default: 30)

        Returns:
            List of dictionaries containing job data

        Raises:
            Exception: Implementation-specific exceptions for request/parsing failures
        """
        pass
