import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from config import BASE_URL, SEARCH_QUERY, MAX_PAGES, TECHNOLOGIES, HEADERS

def scrape_dou_vacancies():
    url = BASE_URL
    headers = HEADERS
    job_list = []

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

                    job_url = title_tag["href"]
                    print(f"Fetching job description URL: {job_url}")

                    try:
                        job_response = requests.get(job_url, headers=headers)
                        job_response.raise_for_status()

                        job_soup = BeautifulSoup(job_response.text, "html.parser")

                        job_description_divs = job_soup.find_all("p")
                        full_description = " ".join([div.get_text(strip=True) for div in job_description_divs])

                        tech_mentions = [tech for tech in TECHNOLOGIES if tech.lower() in full_description.lower()]

                        job_list.append({
                            "title": title,
                            "company": company,
                            "location": location,
                            "description": full_description,
                            "technologies": tech_mentions
                        })

                    except requests.RequestException as e:
                        print(f"Error fetching job description: {e}")
                        continue

        except requests.RequestException as e:
            print(f"Error fetching page data: {e}")
            continue

        time.sleep(7)

    return job_list

def save_to_csv(job_list, filename="vacancies.csv"):
    df = pd.DataFrame(job_list)
    # Перетворення списків в рядки
    df["technologies"] = df["technologies"].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    df = df.drop_duplicates()  # Видалення дублікатів
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    jobs = scrape_dou_vacancies()
    save_to_csv(jobs)
    print(f"Saved {len(jobs)} jobs to CSV.")
