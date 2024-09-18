import requests
from bs4 import BeautifulSoup
import time


def scrape_dou_vacancies():
    url = "https://jobs.dou.ua/vacancies/?search=python"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    jobs = []

    for page in range(1, 5):
        page_url = f"{url}&page={page}"
        print(f"Fetching URL: {page_url}")

        try:
            response = requests.get(page_url, headers=headers)
            response.raise_for_status()
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Length: {len(response.text)}")

            print(response.text[:1000])

            soup = BeautifulSoup(response.text, "html.parser")

            print(soup.prettify()[:1000])

            job_listings = soup.find_all("li", class_="l-vacancy")
            print(f"Found {len(job_listings)} job listings")

            for job in job_listings:
                print(job.prettify()[:500])

                title_tag = job.find("a", class_="vt")
                company_tag = job.find("a", class_="company")
                location_tag = job.find("span", class_="cities")

                if title_tag and company_tag and location_tag:
                    title = title_tag.get_text().strip()
                    company = company_tag.get_text().strip()
                    location = location_tag.get_text().strip()
                    jobs.append({"title": title, "company": company, "location": location})

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            continue

        time.sleep(15)

    return jobs


if __name__ == "__main__":
    jobs = scrape_dou_vacancies()
    print(jobs)
