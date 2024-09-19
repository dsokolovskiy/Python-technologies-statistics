import pandas as pd

df = pd.read_csv("vacancies.csv")

duplicates = df[df.duplicated()]

if not duplicates.empty:
    print("Duplicates found:")
    print(duplicates)

else:
    print("No duplicates")
