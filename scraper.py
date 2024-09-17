import requests

from bs4 import BeautifulSoup


def scrape_djinni_vacancies():
    url = "https://djinni.co/jobs/?primary_keyword=python"
    response = requests.get(url)
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
