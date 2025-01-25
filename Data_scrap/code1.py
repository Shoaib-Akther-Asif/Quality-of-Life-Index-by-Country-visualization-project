from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

def scrape_year(year, driver):
    url = f"https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title={year}"
    driver.get(url)
    time.sleep(1)

    table = driver.find_element(By.ID, "t2")

    # Extract table headers
    headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]

    # Extract table rows
    rows = table.find_elements(By.TAG_NAME, "tr")[1:]
    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        data.append([col.text for col in cols])

    # Create a DataFrame
    df = pd.DataFrame(data, columns=headers)
    return df

def main():
    path = r"C:\Program Files (x86)\chromedriver.exe"  # Update this path as needed
    service = Service(path)
    driver = webdriver.Chrome(service=service)

    try:
        all_data = []

        # Scrape data for the years 2023, 2024, and 2025
        for year in range(2016, 2026):
            print(f"Scraping data for {year}...")
            df = scrape_year(year, driver)
            df["Year"] = year  # Add a column for the year
            all_data.append(df)

        # Combine all data into a single DataFrame
        combined_df = pd.concat(all_data, ignore_index=True)

        # Save the combined DataFrame to a CSV file
        output_file = "quality_of_life_2016_to_2025.csv"
        combined_df.to_csv(output_file, index=False)

        print(f"Data successfully scraped and saved to {output_file}!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
