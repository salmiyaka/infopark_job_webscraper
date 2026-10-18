
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://infopark.in/companies-job"
OUTPUT_FILE = "Infopark_Jobs.xlsx"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; InfoparkJobScraper/1.0)"
}


def scrape_infopark_jobs():
    try:
        print("Connecting to Infopark website...")

        response = requests.get(
            URL,
            headers=HEADERS,
            timeout=15
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")

        if table is None:
            print("Error: No job table found on the webpage.")
            print("The website structure may have changed.")
            return

        data = []

        rows = table.find_all("tr")

        for row in rows[1:]:
            cols = row.find_all("td")

            if len(cols) >= 4:
                date = cols[0].get_text(strip=True)
                job = cols[1].get_text(strip=True)
                company = cols[2].get_text(strip=True)
                last_date = cols[3].get_text(strip=True)

                data.append([
                    date,
                    job,
                    company,
                    last_date
                ])

        if not data:
            print("No job records found. Excel file was not updated.")
            return

        df = pd.DataFrame(
            data,
            columns=[
                "Date",
                "Job Title",
                "Company Name",
                "Last Date"
            ]
        )

        df.to_excel(OUTPUT_FILE, index=False)

        print(f"Successfully collected {len(df)} job records.")
        print(f"Excel file saved as: {OUTPUT_FILE}")

    except requests.exceptions.Timeout:
        print("Error: The website took too long to respond.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Connection error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    scrape_infopark_jobs()











