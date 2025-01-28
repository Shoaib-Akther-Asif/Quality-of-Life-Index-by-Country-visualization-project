# Capstone_project_1
## Problem Statement & findings
The goal of this project is to gather and analyze quality-of-life data by country for 2025, sourced dynamically from the [Numbeo website](https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=2025). This project involved scraping the data using Selenium, followed by processing and visualizing it through interactive dashboards in Tableau Public.

### **Goals of This Project**

1. Provide a comprehensive global perspective on various quality-of-life indices.  
2. Identify key factors influencing the `Quality of Life Index`.  
3. Compare different indices to determine the best country for living.  
4. Analyze patterns of quality-of-life-related indices across different continents.  
5. Create a heatmap to visually represent the best countries to live in.  

### The following key insights and analyses were derived using the data and presented through the Tableau Dashboard:
## Describing Tableau Dashboard and Sheets

### 1. **World-wide View for Selected Index**
A dynamic world map visualizing various indexes over time, labeled for clarity.  
- Users can explore details by selecting specific years, countries, and indexes.  
- Multiple countries and years can be selected, with the average index value displayed for multi-year selections.

---

### 2. **Correlation of Different Indexes**
This sheet highlights correlations between various indexes.  
- Users can select single or multiple values to analyze the relationships among the indexes dynamically.

---

### 3. **Correlation with Quality of Life**
Analyze index patterns related to the `Quality of Life Index`.  
- Users can select specific year(s) to examine how other indexes interact with quality of life over time.

---

### 4. **Top 20 Best Places to Live**
This visualization identifies the top 20 countries to live in.  
- Users can select single or multiple years to refine the results and adjust index weights for customized analysis.  
- The `Select Index` option allows users to view specific values for chosen years.  

**Calculated Field Formula Used:**
```bash
([Quality of Life Index] * [Quality Idx]) + 
([Safety Index] * [Safety_idx]) +
([Health Care Index] * [Health_idx]) -
([Pollution Index] * [Pollution_idx]) -
([Cost of Living Index] * [Cost_of_living_Idx])
```
### 5. **Top 20 Places You May Not Want to Live**
This sheet identifies the 20 worst countries to live in using the same calculated field as the "Top 20 Best Places to Live" sheet.  
- Users can select single or multiple years and adjust index weights for customized analysis.  
- The `Select Index` option allows users to view specific index values for the chosen years.

---

### 6. **Country Overview**
A line chart showcasing the values of all indexes over time for selected countries.  
- Users can use drop-down menus to select specific countries and year(s) to analyze trends and patterns.

---

### 7. **Asian Countries Trend Over Time on Different Indexes**
This visualization displays trends of various indexes over time for Asian countries.  
- Users can select year(s) to examine patterns and changes in index values.

---

### 8. **European Countries Trend Over Time on Different Indexes**
This visualization shows trends of various indexes over time for European countries.  
- Users can select specific year(s) to analyze the patterns and changes in index values.

---

### 9. **Top 50 Countries: Quality of Life, Pollution, and Traffic Commute Time Heatmap**
A heatmap focusing on the top 50 countries filtered by their `Quality of Life Index`.  
- Establishes relationships between the `Pollution Index` and `Quality of Life Index`.  
- **Bubble size** represents the `Pollution Index`, while **color intensity** reflects the `Quality of Life Index`.

## Findings

### 1. **For (Year = All)**  
#### Dashboard: *Factors of Quality of Life*  
- **Upper Left:**  
  The world map displays the average values of the selected index for all years.  

- **Upper Right:**  
  We observed the following correlations with the `Quality of Life Index`:  
  - Positive correlations:  
    - `Purchasing Power Index` (**Strong**): `0.813728`  
    - `Cost of Living Index` (**Moderate**): `0.665700`  
  - Negative correlations:  
    - `Pollution Index` (**Strong**): `-0.853893`  
    - `Traffic Commute Time Index` (**Moderate**): `-0.675780`  

- **Lower Left:**  
  Among **Asian countries**, the highest-ranked countries for various indices were:  
  - `Quality of Life Index`: **Oman** (`182.3`)  
  - `Cost of Living Index`: **Singapore** (`82.49`)  
  - `Purchasing Power Index`: **Qatar** (`123.3`)  
  - `Pollution Index`: **Lebanon** (`88.46`)  
  - `Traffic Commute Time Index`: **Sri Lanka** (`59.36`) and **Bangladesh** (`57.22`)  

- **Lower Right:**  
  Among **European countries**, the highest-ranked countries for various indices were:  
  - `Quality of Life Index`: **Luxembourg** (`198.48`)  
  - `Cost of Living Index`: **Norway** (`96.60`)  
  - `Purchasing Power Index`: **Luxembourg** (`139.8`)  
  - `Pollution Index`: **North Macedonia** (`80.93`)  
  - `Traffic Commute Time Index`: **Russia** (`45.3`)  

---

### 2. **For (Year = 2025) with All Indexes Maximized**  
#### Dashboard: *Country Comparison*  
- The **best country to live in** was **Netherlands**, with a `Quality of Life Index` value of `211.30`.  
- The **worst country to live in** was **Nigeria**, where the `Quality of Life Index` never exceeded `60`.  
- **Heatmap Insights:**  
  - **Luxembourg** ranked highest with a `Quality of Life Index` of `220.1` and a `Pollution Index` of `23.3`.  
  - Other top countries included:  
    - **Finland**: (`203.8`, `11.8`)  
    - **Denmark**: (`209.9`, `20.6`)  

### You can check the [Analysis file here](https://colab.research.google.com/drive/14FMUSrk4QUSyd7dLtZfdPpcA6sfFx0d3?usp=sharing).
### All insights are presented in an interactive and user-friendly Tableau sheets and dashboards, which can be accessed here: [Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/md.shoaib.akther.asif/viz/Capstone_project_1_17378065386910/Factorsofqualityoflife)

## Build From Sources and Run the Selenium Scraper

### Steps to Get Started:

1. **Clone the Repository, Set Up Environment, and Run the Scraper**
   - Clone the repository:
     ```bash
     git clone https://github.com/Shoaib-Akther-Asif/Capstone_project_1.git
     ```
   - Initialize and activate a virtual environment:
     ```bash
     virtualenv --no-site-packages venv
     source venv/bin/activate
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Download the compatible version of Chrome WebDriver from the [official website](https://chromedriver.chromium.org/downloads).  
   - Run the scraper:
     ```bash
     python Data_scrap/code1.py --chromedriver_path <path_to_chromedriver>
     ```

   After completing these steps, you will get a file named `quality_of_life_2016_to_2025.csv` containing data from 2016 to 2025 for all required fields.

2. **Alternatively**  
   You can check the pre-scraped data [here](https://github.com/Shoaib-Akther-Asif/Capstone_project_1/blob/main/Data_scrap/quality_of_life_2016_to_2025.csv).
