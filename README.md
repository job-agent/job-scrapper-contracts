# Job Scrapper Contracts

Contract definitions for job scrapper services. This package provides standardized data models for job listings that can be shared between scrapper services and consumers.

## Installation

```bash
pip install job-scrapper-contracts
```

For development:
```bash
pip install job-scrapper-contracts[dev]
```

## Features

- Type-safe data models for job listings
- Both dataclass and TypedDict formats supported
- Comprehensive job information fields (title, company, location, salary, etc.)
- Built-in serialization methods
- Full type hints for better IDE support

## Usage

### Basic Usage

```python
from job_scrapper_contracts.models import Job, Company, Location, Salary
from datetime import datetime

# Create a job listing
job = Job(
    job_id=12345,
    title="Senior Python Developer",
    url="https://example.com/jobs/12345",
    description="We are looking for an experienced Python developer...",
    company=Company(
        name="Tech Corp",
        website="https://techcorp.com"
    ),
    category="Software Development",
    date_posted=datetime.now(),
    valid_through=datetime(2025, 12, 31),
    employment_type="FULL_TIME",
    salary=Salary(
        currency="USD",
        min_value=100000,
        max_value=150000
    ),
    location=Location(
        country="United States",
        locality=["San Francisco"],
        region="CA",
        is_remote=True
    ),
    experience_months=36.0,
    industry="Technology"
)

# Convert to dictionary for serialization
job_dict = job.to_dict()
print(job)  # Job(id=12345, title='Senior Python Developer', company='Tech Corp')
```

### Working with TypedDict

`JobDict` uses TypedDict inheritance to enforce required and optional fields:
- **JobDictRequired**: Contains required fields that must always be present
- **JobDict**: Extends JobDictRequired and adds optional fields

```python
from job_scrapper_contracts.models import JobDict, CompanyDict, LocationDict, SalaryDict

# Minimal JobDict with only required fields
minimal_job: JobDict = {
    'job_id': 12345,
    'title': 'Senior Python Developer',
    'url': 'https://example.com/jobs/12345',
    'description': 'Job description...',
    'company': {
        'name': 'Tech Corp',
        'website': 'https://techcorp.com'
    },
    'date_posted': '2025-01-15T10:00:00',
    'valid_through': '2025-12-31T23:59:59',
    'employment_type': 'FULL_TIME'
}

# Full JobDict with optional fields included
full_job: JobDict = {
    'job_id': 12345,
    'title': 'Senior Python Developer',
    'url': 'https://example.com/jobs/12345',
    'description': 'Job description...',
    'company': {
        'name': 'Tech Corp',
        'website': 'https://techcorp.com'
    },
    'date_posted': '2025-01-15T10:00:00',
    'valid_through': '2025-12-31T23:59:59',
    'employment_type': 'FULL_TIME',
    # Optional fields below
    'category': 'Software Development',
    'salary': {
        'currency': 'USD',
        'min_value': 100000,
        'max_value': 150000
    },
    'location': {
        'country': 'United States',
        'locality': ['San Francisco'],
        'region': 'CA',
        'postal_code': None,
        'is_remote': True
    },
    'experience_months': 36.0,
    'industry': 'Technology',
    'source': 'linkedin'
}
```

## Data Models

### Job

The main job listing model with the following fields:

**Required fields:**
- `job_id` (int): Unique identifier for the job
- `title` (str): Job title
- `url` (str): URL to the job posting
- `description` (str): Full job description
- `company` (Company): Company information
- `date_posted` (datetime): When the job was posted
- `valid_through` (datetime): Job posting expiration date
- `employment_type` (str): Type of employment (e.g., FULL_TIME, PART_TIME, CONTRACT)

**Optional fields:**
- `category` (str): Job category
- `salary` (Salary): Salary information
- `experience_months` (float): Required experience in months
- `location` (Location): Job location details
- `industry` (str): Industry sector
- `source` (str): Job board source (e.g., 'djinni', 'linkedin')

### Company

Company information model:
- `name` (str): Company name
- `website` (Optional[str]): Company website URL

### Location

Location information model:
- `country` (Optional[str]): Country name
- `locality` (Optional[List[str]]): City or locality names
- `region` (Optional[str]): State or region
- `postal_code` (Optional[str]): Postal/ZIP code
- `is_remote` (bool): Whether the position is remote (defaults to False)

### Salary

Salary information model:
- `currency` (str): Currency code (e.g., USD, EUR)
- `min_value` (Optional[float]): Minimum salary
- `max_value` (Optional[float]): Maximum salary

## Development

### Setup

Clone the repository and install development dependencies:

```bash
git clone <repository-url>
cd job_scrapper_contracts
pip install -e .[dev]
```

### Code Quality

The project uses the following tools:
- **black**: Code formatting (line length: 100)
- **ruff**: Linting
- **mypy**: Type checking

Run formatting:
```bash
black src/
```

Run linting:
```bash
ruff check src/
```

Run type checking:
```bash
mypy src/
```

## Requirements

- Python >= 3.8

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please ensure that:
1. Code is formatted with black
2. Type hints are provided for all functions
3. All mypy checks pass
4. Code follows the existing style and conventions

## Project Structure

```
job_scrapper_contracts/
 src/
    job_scrapper_contracts/
        __init__.py
        models.py          # Data models and contracts
 pyproject.toml             # Project configuration
 README.md                  # This file
```
