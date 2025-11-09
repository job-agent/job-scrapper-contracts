from typing import Optional, TypedDict


class ScrapeJobsFilter(TypedDict, total=False):
    min_salary: Optional[int]
    employment_location: Optional[str]
    posted_after: Optional[str]
