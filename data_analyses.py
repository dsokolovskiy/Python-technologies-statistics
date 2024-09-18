import pandas as pd
import matplotlib.pyplot as plt
import json

# Ключові слова технологій
tech_keywords = {
    "Python": ["Python"],
    "Django": ["Django"],
    "Flask": ["Flask"],
    "React": ["React"],
    "JavaScript": ["JavaScript", "JS"],
    "Machine Learning": ["Machine Learning", "ML"],
    "DevOps": ["DevOps", "Continuous Integration", "Continuous Deployment", "CI/CD"],
    "SQL": ["SQL", "PostgreSQL", "MySQL", "MariaDB"],
    "NoSQL": ["NoSQL", "MongoDB", "Cassandra", "Redis"],
    "AWS": ["AWS", "Amazon Web Services"],
    "Azure": ["Azure", "Microsoft Azure"],
    "Docker": ["Docker"],
    "Kubernetes": ["Kubernetes"],
    "Java": ["Java"],
    "C++": ["C++"],
    "Node.js": ["Node.js"],
    "PHP": ["PHP"],
    "Ruby": ["Ruby"],
    "GraphQL": ["GraphQL"],
    "Terraform": ["Terraform"],
    "Cloud": ["Cloud"],
    "Microservices": ["Microservices"],
    "REST": ["REST", "RESTful"],
    "AI": ["AI", "Artificial Intelligence"]
}

df = pd.read_csv("vacancies.csv")

# Функція для отримання технологій з опису вакансії
def extract_technologies_from_description(description):
    description = description.lower()
    found_techs = []
    for tech, keywords in tech_keywords.items():
        if any(keyword.lower() in description for keyword in keywords):
            found_techs.append(tech)
    return found_techs

# Функція для перетворення рядків у списки
def parse_technologies(tech_str):
    if isinstance(tech_str, str):
        if tech_str == "[]":
            return []
        try:
            return json.loads(tech_str)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {tech_str}")
            return tech_str.split(", ")  # Можливо, просте розділення
    return []

df["technologies"] = df["technologies"].apply(parse_technologies)

# Оновлення технологій на основі опису вакансії, якщо в колонці 'technologies' порожньо
df["technologies"] = df.apply(
    lambda row: row["technologies"]
    if row["technologies"]
    else extract_technologies_from_description(row["description"]),
    axis=1
)

# Підрахунок частоти згадуваних технологій
all_techs = [tech for sublist in df["technologies"] for tech in sublist]
technology_counts = pd.Series(all_techs).value_counts()

print("Technology counts:")
print(technology_counts)

# Побудова графіка
plt.figure(figsize=(12, 8))
bars = plt.bar(technology_counts.index, technology_counts.values, color="skyblue")

# Додавання підписів до барів
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(height),
        ha="center",
        va="bottom"
    )

plt.title("Frequency of Technologies Mentioned in Job Listings")
plt.xlabel("Technology")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("technology_frequency.png")
plt.show()
