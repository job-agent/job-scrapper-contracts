"""
Data models for job listings - Contract definitions

These models define the contract between scrapper services and consumers.
"""

from dataclasses import dataclass
from typing import Optional, TypedDict
from datetime import datetime


class SalaryDict(TypedDict):
    """Salary information dictionary"""

    currency: str
    min_value: Optional[float]
    max_value: Optional[float]


class CompanyDict(TypedDict):
    """Company information dictionary"""

    name: str
    website: Optional[str]


class LocationDict(TypedDict):
    """Location information dictionary"""

    region: Optional[str]
    is_remote: bool
    can_apply: Optional[bool]


class JobDict(TypedDict, total=False):
    """Job listing dictionary structure"""

    job_id: int
    title: str
    url: str
    description: str
    company: CompanyDict
    category: str
    date_posted: str  # ISO format datetime string
    valid_through: str  # ISO format datetime string
    employment_type: str
    # Optional fields
    salary: SalaryDict
    experience_months: float
    location: LocationDict
    industry: str


@dataclass
class Salary:
    """Salary information for a job"""

    currency: str
    min_value: Optional[float] = None
    max_value: Optional[float] = None


@dataclass
class Company:
    """Company/organization information"""

    name: str
    website: Optional[str] = None


@dataclass
class Location:
    """Job location information

    Attributes:
        region: Geographic region or country for the job
        can_apply: Indicates whether the user can apply for this job based on location.
            - True: User can apply (bi-check2-circle or bi-question-circle icon)
            - False: User cannot apply (bi-x-circle icon)
            - None: Status unknown or not available
    """

    region: Optional[str] = None
    is_remote: bool = False
    can_apply: Optional[bool] = None


@dataclass
class Job:
    """Job listing data model"""

    job_id: int
    title: str
    url: str
    description: str
    company: Company
    category: str
    date_posted: datetime
    valid_through: datetime
    employment_type: str

    # Optional fields
    salary: Optional[Salary] = None
    experience_months: Optional[float] = None
    location: Optional[Location] = None
    industry: Optional[str] = None
    direct_apply: bool = True

    def __str__(self):
        return f"Job(id={self.job_id}, title='{self.title}', company='{self.company.name}')"

    def to_dict(self) -> JobDict:
        """Convert job to dictionary"""
        result: JobDict = {
            "job_id": self.job_id,
            "title": self.title,
            "url": self.url,
            "description": self.description,
            "company": {"name": self.company.name, "website": self.company.website},
            "category": self.category,
            "date_posted": self.date_posted.isoformat(),
            "valid_through": self.valid_through.isoformat(),
            "employment_type": self.employment_type,
        }

        if self.salary:
            salary_dict: SalaryDict = {
                "currency": self.salary.currency,
                "min_value": self.salary.min_value,
                "max_value": self.salary.max_value,
            }
            result["salary"] = salary_dict

        if self.location:
            location_dict: LocationDict = {
                "region": self.location.region,
                "is_remote": self.location.is_remote,
                "can_apply": self.location.can_apply,
            }
            result["location"] = location_dict

        if self.experience_months is not None:
            result["experience_months"] = self.experience_months

        if self.industry:
            result["industry"] = self.industry

        return result
