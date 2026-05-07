# CSV Data Cleaner & Validator

A practical Python project for cleaning, validating, and exporting messy CSV files.

This repository is designed as a portfolio-ready example for clients who need to clean business data before reporting, import, analysis, or automation.

## What This Project Does

The tool reads a messy CSV file, cleans the data, validates required columns, detects missing values, removes duplicate rows, and exports a clean CSV file.

## Features

- Read CSV files
- Normalize column names
- Trim extra spaces from text values
- Remove fully empty rows
- Remove duplicate rows
- Validate required columns
- Count missing values
- Generate a validation summary
- Export a cleaned CSV file

## Folder Structure

```text
csv-data-cleaner-validator/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── sample_data/
│   └── messy_customers.csv
├── src/
│   └── csv_cleaner_validator/
│       ├── __init__.py
│       └── cleaner.py
├── examples/
│   └── run_demo.py
├── tests/
│   └── test_cleaner.py
├── docs/
│   └── project-overview.md
└── output/
    └── .gitkeep
```

## Requirements

- Python 3.10+
- pandas
- pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Demo

```bash
python examples/run_demo.py
```

The cleaned CSV file will be saved here:

```text
output/clean_customers.csv
```

## Required Columns

The demo validates these columns:

```text
customer_id, name, email, country, signup_date
```

## Business Use Cases

This project can be adapted for:

- Customer data cleanup
- Sales lead CSV validation
- CRM import preparation
- E-commerce order exports
- Marketing contact lists
- Reporting workflows
- Data quality checks before automation

## Freelance Service Angle

This repository demonstrates a real service I can provide:

> I can build Python tools that clean messy CSV files, validate required fields, remove duplicates, and prepare business data for reports, dashboards, or system imports.

## Related Portfolio Pages

- Portfolio: https://farshidghaffari.net
- Excel / CSV Automation Service: https://farshidghaffari.net/services/excel-csv-automation/
- Projects: https://farshidghaffari.net/projects/
- Blog: https://farshidghaffari.net/blog/

## Author

Farshid Ghaffari  
Python Developer — Automation, Backend APIs, Data Tools

Website: https://farshidghaffari.net  
GitHub: https://github.com/farshidghaffari
