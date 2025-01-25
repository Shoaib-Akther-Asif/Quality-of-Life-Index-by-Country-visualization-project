# Capstone_project_1


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
