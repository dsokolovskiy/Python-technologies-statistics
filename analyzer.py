import pandas as pd

import matplotlib.pyplot as plt


def analyze_vacancies(vacancies):
    df = pd.DataFrame(vacancies)
    technology_counts = df["title"].value_counts()

    plt.figure(figsize=(10, 6))
    technology_counts.plot(kind="bar")
    plt.xlabel("Technology")
    plt.ylabel("Number of Vacancies")
    plt.title("Technology Demand")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("technology_demand.png")


if __name__ == "__main__":
    from scraper import scrape_djinni_vacancies
    jobs = scrape_djinni_vacancies()
    analyze_vacancies(jobs)
