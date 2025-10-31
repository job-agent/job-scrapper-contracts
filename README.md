# Job Scrapper Contracts

Contract definitions for job scrapper services. This package provides:

- **Data Models**: Type-safe models for job listings, companies, salaries, and locations
- **Abstract Interface**: `JobScrapperInterface` that all scrapper implementations must follow
- **TypedDict Definitions**: Dictionary structures for serialization/deserialization

## Purpose

This package serves as a contract between:
- **Scrapper Services** (e.g., djinni-scrapper, linkedin-scrapper): Implement the interface
- **Consumer Services**: Depend on the interface without coupling to specific implementations

## Installation

```bash
# Install from local path (during development)
pip install -e /path/to/job-scrapper-contracts

# Or install from git (when published)
pip install git+https://github.com/yourusername/job-scrapper-contracts.git
```

## Usage

### For Scrapper Implementations

```python
from job_scrapper_contracts import JobScrapperInterface, Job, JobDict
from typing import List

class DjinniScrapper(JobScrapperInterface):
    def scrape_jobs(
        self,
        salary: int = 4000,
        employment: str = "remote",
        page: int = 1,
        timeout: int = 30
    ) -> List[Job]:
        # Implementation here
        pass

    def scrape_jobs_as_dicts(
        self,
        salary: int = 4000,
        employment: str = "remote",
        page: int = 1,
        timeout: int = 30
    ) -> List[JobDict]:
        # Implementation here
        pass
```

### For Consumer Services

```python
from job_scrapper_contracts import JobScrapperInterface, Job

def process_jobs(scrapper: JobScrapperInterface):
    """Process jobs from any scrapper implementation"""
    jobs = scrapper.scrape_jobs(salary=5000)
    for job in jobs:
        print(f"{job.title} at {job.company.name}")
```

## Models

### Job
Main job listing model with all job details.

### Company
Company/organization information.

### Salary
Salary range information.

### Location
Job location details including remote work flag.

## Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run type checking
mypy src/job_scrapper_contracts

# Format code
black src/job_scrapper_contracts
```

## License

MIT
