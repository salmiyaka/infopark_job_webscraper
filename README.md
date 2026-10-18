# Infopark Job Web Scraper

A Python project to collect Infopark job vacancy details and save them in an Excel file.

## Overview

This project extracts job vacancy information from the Infopark website using Python web scraping techniques. The collected data is organized in an Excel spreadsheet for easy reference.

## Features

- Extracts job posting dates
- Collects job titles and company names
- Retrieves application deadlines
- Exports the collected data to Excel
- Organizes job information into structured columns

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- OpenPyXL

## Project Structure

```text
infopark_job_webscraper/
├── webscrap.py
├── requirements.txt
├── Infopark_Jobs.xlsx
├── README.md
└── .gitignore
```

## Installation

1. Install Python 3.
2. Clone or download this repository.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Execute the following command in the project directory:

```bash
python webscrap.py
```

The script saves the extracted job details in `Infopark_Jobs.xlsx`.

## Data Fields

- Date
- Job Title
- Company Name
- Last Date

