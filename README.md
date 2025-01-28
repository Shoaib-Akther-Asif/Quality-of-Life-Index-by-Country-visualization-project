# Capstone_project_1
## Problem Statement & findings
The goal of this project is to gather and analyze quality-of-life data by country for 2025, sourced dynamically from the [Numbeo website](https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=2025). This project involved scraping the data using Selenium, followed by processing and visualizing it through interactive dashboards in Tableau Public.

### The following key insights and analyses were derived using the data and presented through the Tableau Dashboard:
1. ```Sheet name ➔ World-wide view for selected index:``` <br> A world map highlighting different indexes over time as label. From this, detailed view of information can be shown as by year and country. Its a dynamic dashboard, all country, year and inedx want to see can be select by user.User can select Multiple `country` and `year` at a time, if multiple year selected then it shows `avgerage` of selected index value.<br>
2. ```Sheet name ➔ Correlation of different index:``` This sheet is about the `correlation` among indexes. Like prevoius user can select single or multiple value to see `Correlation` of indexes.<br>
3. ```Sheet name ➔ Correlation with quality of life:``` From this sheet user can select year(s) to see the indexes pattern related to `Quality of life`.<br>
4. ```Sheet name ➔ Top 20 Best Place to Live:``` This figure is about to find the best country to live (top 20). User can select single or miltiple year to find the best places to live, also can adjust the indexes. Users  can also select a index from `Select Index` option to see selected index value for selected year(s).<br>For this viz the following code is used to create a calculated field:<br>
```bash
([Quality of Life Index] * [Quality Idx]) + 
([Safety Index] * [Safety_idx]) +
([Health Care Index] * [Health_idx]) -
([Pollution Index] * [Pollution_idx]) -
([Cost of Living Index] * [Cost_of_living_Idx])
```
5. ```Sheet name ➔ Top 20  Place where u may not want to Live:``` This figure is about to find the worst country to live (top 20).The previous calculated filed is used in this viz also. Like previous viz, User can select single or miltiple year to find the best places to live, also can adjust the indexes. Users  can also select a index from `Select Index` option to see selected index value for selected year(s).<br>
6.  ```Sheet name ➔ Country Overview:``` This viz Shows value for every indexes over time. User can select year(s) and countries from drop-down to see the pattern in a line chart among countries.<br>
7. ```Sheet name ➔ Asian countries Trend over time on different Index:``` Shows value of diffrenet indexes over time for `Asian countries`. User can select year(s) to find the pattern for indexes over time.<br>
8. ```Sheet name ➔ Europian countries Trend over time on different Index:``` Shows value of diffrenet indexes over time for `Europian countries`. User can select year(s) to find the pattern for indexes over time.<br>
9. ```Sheet name ➔ Top 50 Quality of life index Countries Pollution and Traffic Commute time Heatmap:``` Top 50 countries filltered from this heatmap. Setting relation between `Pollution Index` and `Quality of life Index`. sized by `Pollution Index` and colored by `Quality of life Index` <br>
#### All insights are presented in an interactive and user-friendly Tableau sheets and dashboards, which can be accessed here: [Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/md.shoaib.akther.asif/viz/Capstone_project_1_17378065386910/World-wideviewforselectedindex)
### Findings:
1. ***For (Year = All)*** <br>From ```Sheet name ➔ Correlation with quality of life:``` The `Quality of Life Index` positively correlates with the `Purchasing Power Index` and `Cost of Living Index`, and a strongly negative correlation with the `Pollution Index`.<br>

2. From ```Sheet name ➔ :Top 20 Best Place to Live```<br>***For (Year = 2025) setting all index max*** <br> The best country to live with was **`Netherland`** with `Quality of life index` value `211.30`. <br>***For (Year = All)***<br> The best country to live with was **`Finland`**<br>

3. From ```Sheet name ➔ :Top 20  Place where u may not want to Live:``` <br>***For (Year = All and Year = 2025 ) & setting all index max***<br> **`Nigeria`** was the worst country to live in, with a `Quality of Life Index` never exceeding 60.<br>

4. From ```Sheet name ➔ Asian countries Trend over time on different Index:``` ***For (Year = All)*** <br> Among Asian countries, the higest countries for different indexes was: <br>  `Quality of life index` ➔ `Oman` with an average value of `182.3` <br> `Cost of living Index` ➔ `Hong Kong(china)` and `Singapore` with an average value of `79.44` and `82.49` <br> `Puchasing power Index` ➔ `Qatar`with an average value of `123.3`<br> `Property price to income ratio` ➔ `Hong-Kong` with an average value of`43.4`
5. From ```Sheet name ➔ Europian countries Trend over time on different Index:``` ***For (Year = All)*** <br> Among Europian countries, the lowest countries for different indexes was: <br>  `Quality of life index` ➔ `Albania` with an average value of `102.4` <br> `Cost of living Index` ➔ `Ukrain`  with an average value of `28.6` <br> `Puchasing power Index` ➔ `Ukraine` with an average value of `33.6`<br> `Property price to income ratio` ➔ `Iceland` with a value `6.47`
6. From ```Top 50 Quality of life index Countries Pollution and Traffic Commute time Heatmap:``` ***For (Year = 2025)*** <br>Among the top 50 countries, **`Luxembourg`** ranked highest with a `Quality of Life Index` of `220.1` and a `Pollution Index` of `23.3`. Other top countries included **Finland** `(203.8, 11.8)` and **Denmark** `(209.9, 20.6)`.
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
Alternatively, check my scraped data [Here](https://github.com/Shoaib-Akther-Asif/Capstone_project_1/blob/main/Data_scrap/quality_of_life_2016_to_2025.csv)
