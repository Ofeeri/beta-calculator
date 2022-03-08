from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from typing import List


def fetch_prices_csv(queries: List) -> List[pd.DataFrame]:
    path = "C:\Program Files (x86)\chromedriver.exe"  # not dynamic
    dataframes = []
    driver = webdriver.Chrome(path)
    for query in queries:
        ticker = query[0]
        timeframe = query[1]
        frequency = query[2]
        driver.get(f'https://finance.yahoo.com/quote/{ticker}/history?p={ticker}&frequency={frequency}')
        time_period = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='C($linkColor) Fz(14px)']")))
        time_period.click()
        driver.find_element(By.XPATH, f"//span[contains(text(), '{timeframe}')]").click()
        driver.find_element(By.XPATH, '//span[text()="Apply"]').click()
        download_link = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').get_attribute("href")
        dataframes.append(pd.read_csv(download_link))
    driver.close()
    return dataframes
