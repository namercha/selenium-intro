from selenium import webdriver
from selenium.webdriver.common.by import By

# Gets the number of articles in English from the wikipedia home page
chrome_driver_path = "/Users/nabil/Documents/code/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)
