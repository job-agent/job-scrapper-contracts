"""
Job Scrapper Contracts

This package defines the contracts (interfaces and data models) for job scrapper services.
Both scrapper implementations and consumer services should depend on this package.
"""

from .models import (
    Job,
    Company,
    Salary,
    Location,
    JobDict,
    CompanyDict,
    SalaryDict,
    LocationDict,
)
from .interface import JobScrapperInterface

__version__ = "0.1.0"

__all__ = [
    # Data models
    "Job",
    "Company",
    "Salary",
    "Location",
    # TypedDict models
    "JobDict",
    "CompanyDict",
    "SalaryDict",
    "LocationDict",
    # Interface
    "JobScrapperInterface",
]
