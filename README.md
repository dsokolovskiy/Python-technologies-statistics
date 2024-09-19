# Python Technologies Statistics

## Overview

The **Python Technologies Statistics** project analyzes and visualizes the most demanded technologies for Python developers based on job vacancies. This project involves scraping job vacancy data, processing it to identify and count mentions of various technologies, and visualizing the results with graphs. The repository contains all the necessary code and resources to perform the analysis and generate visualizations.

## Project Structure

The project directory includes:

- `data_analyses.py`: Script for analyzing job data and generating visualizations.
- `check_duplicates.py`: Script for checking and removing duplicate job entries.
- `scraper.py`: Script for scraping job vacancy data from websites.
- `vacancies.csv`: Sample CSV file containing job vacancy data.
- `technology_frequency.png`: Output image showing the frequency of mentioned technologies.
- `requirements.txt`: File listing Python dependencies.
- `README.md`: This file.
- `.gitignore`: Git ignore file to exclude unnecessary files from the repository.

## Technologies Used

- **Python 3.12**
- **pandas 2.0.0**
- **matplotlib 3.7.1**
- **beautifulsoup4 4.12.2**
- **requests 2.31.0**

## Requirements

To install the necessary Python packages, use the `requirements.txt` file:

```bash
pip install -r requirements.txt
```


## Project Installation

1. Clone the Repository
```bash
git clone https://github.com/dsokolovskiy/Python-technologies-statistics.git
cd PythonTecnhologiesStatistics
```


2. Run the Scraper


The `scraper.py`script collects job vacancy data from specified websites and saves it to `vacancies.csv`. Make sure to configure the scraper according to the target websites.
```bash
python scraper.py
```

3. Prepare the Data
Ensure that the `vacancies.csv` file contains the following columns: `title`, `company`, `location`, `description` and `technologies`.



4. Run the Analysis 
Execute the `data_analyses.py` script to perform the analysis and generate visualizations:
```bash
python data_analyses.py
```
This will generate a PNG image named `technology_frequency.png`, which visualizes the frequency of different technologies mentioned in job listings.



5. Check for Duplicates

To check for and remove duplicate entries in your CSV file, use the `check_duplicates.py` script:
```bash
python check_duplicates.py
```
The script will clean your dataset by removing any duplicate job entries based on their descriptions.


## Results

The `data_analyses.py` script produces a bar chart image `technology_frequency.png` that visualizes the frequency of different technologies mentioned in job listings. This chart helps in understanding which technologies are most frequently sought after in job postings for Python developers.

## Contributing

Contributions are welcome! If you have suggestions for improvements of additional features, please submit a pull request or open an issue.