import requests

from bs4 import BeautifulSoup

from config import DJINNI_URL


def scrape_djinni_vacancies():
    response = requests.get(DJINNI_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    vacancies = []
    for job in soup.find_all("div", class_="profile"):
        title = job.find("a", class_="profile-link").text
        company = job.find("div", class_="company").text
        vacancies.append({"title": title, "company": company})

    return vacancies


if __name__ == "__main__":
    jobs = scrape_djinni_vacancies()
    print(jobs)
