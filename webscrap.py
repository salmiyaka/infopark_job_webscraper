import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://infopark.in/companies-job"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

data = []

rows = table.find_all("tr")

for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 4:
        date = cols[0].text.strip()
        job = cols[1].text.strip()
        company = cols[2].text.strip()
        last_date = cols[3].text.strip()

        data.append([date, job, company, last_date])

df = pd.DataFrame(
    data,
    columns=["Date", "Job Title", "Company Name", "Last Date"]
)

df.to_excel("Infopark_Jobs.xlsx", index=False)

print("Excel file created successfully!")













