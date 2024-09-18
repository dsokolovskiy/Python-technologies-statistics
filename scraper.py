import requests
from bs4 import BeautifulSoup
import time
import csv
from config import BASE_URL, SEARCH_QUERY, MAX_PAGES, TECHNOLOGIES, HEADERS


def scrape_dou_vacancies():
    url = BASE_URL
    headers = HEADERS

    jobs = []

    for page in range(1, MAX_PAGES + 1):
        page_url = f"{url}?search={SEARCH_QUERY}&page={page}"
        print(f"Fetching URL: {page_url}")

        try:
            response = requests.get(page_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            job_listings = soup.find_all("li", class_="l-vacancy")

            for job in job_listings:
                title_tag = job.find("a", class_="vt")
                company_tag = job.find("a", class_="company")
                location_tag = job.find("span", class_="cities")

                if title_tag and company_tag and location_tag:
                    title = title_tag.get_text().strip()
                    company = company_tag.get_text().strip()
                    location = location_tag.get_text().strip()
                    description = job.find("div", class_="sh-info").get_text(strip=True) if job.find("div",
                                                                                                     class_="sh-info") else ''

                    tech_mentions = [tech for tech in TECHNOLOGIES if tech.lower() in description.lower()]

                    jobs.append({"title": title, "company": company, "location": location, "description": description,
                                 "technologies": tech_mentions})

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            continue

        time.sleep(7)  # Затримка 2 секунди між запитами

    return jobs


def save_to_csv(jobs, filename='vacancies.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'company', 'location', 'description', 'technologies']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for job in jobs:
            writer.writerow(job)


if __name__ == "__main__":
    jobs = scrape_dou_vacancies()
    save_to_csv(jobs)
    print(f"Saved {len(jobs)} jobs to CSV.")
