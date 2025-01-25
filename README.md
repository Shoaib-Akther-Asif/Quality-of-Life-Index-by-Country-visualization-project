# Capstone_project_1
## Problem Statement
The goal of this project is to gather and analyze quality-of-life data by country for 2025, sourced dynamically from the [Numbeo website](https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=2025). This project involved scraping the data using Selenium, followed by processing and visualizing it through interactive dashboards in Tableau Public.

### The following key insights and analyses were derived using the data and presented through the Tableau Dashboard:
1. ```Sheet name ➔ World-wide view for selected index:``` <br> A world map highlighting different indexes over time as label. From this, detailed view of information can be shown as by year and country. Its a dynamic dashboard, all country, year and inedx want to see can be select by user.
2. ```Sheet name ➔ Correlation of different index:```A bar chart showcasing the countries with the highest average quality-of-life scores.
3.Regional analysis for European countries, excluding Russia, to uncover variations in quality of life across the region.
4.An analysis of factors (e.g., purchasing power, safety, health care, cost of living) directly correlated with the overall quality-of-life score, aiming to understand the metrics driving these rankings.
5.Insights into specific countries or regions, such as which countries consistently perform well across multiple indices.
All insights are presented in an interactive and user-friendly Tableau dashboard, which can be accessed here: [Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/md.shoaib.akther.asif/viz/Capstone_project_1_17378065386910/World-wideviewforselectedindex)



## Build From Sources and Run the Selenium Scraper
1. Clone the repo
```bash
git clone : https://github.com/Shoaib-Akther-Asif/Capstone_project_1.git
```
2. Intialize and activate virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads
5. Run the scraper
```bash
python Data_scrap/code1.py --chromedriver_path <path_to_chromedriver>
```
6.You will get a file named quality_of_life_2016_to_2025.csv containing data from year 2016 to 2025 for all the required fields.
Alternatively, check my scraped data here: https://github.com/Shoaib-Akther-Asif/Capstone_project_1/blob/main/Data_scrap/quality_of_life_2016_to_2025.csv

Tableau Public View: https://public.tableau.com/app/profile/md.shoaib.akther.asif/viz/Capstone_project_1_17378065386910/World-wideviewforselectedindex
