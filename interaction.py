from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Gets the number of articles in English from the wikipedia home page
chrome_driver_path = "/Users/nabil/Documents/code/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

# Click on a link
article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All Portals")
# all_portals.click()

# Typing in a search bar. This searches for "Python" in the search bar in wikipedia front page.
search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
