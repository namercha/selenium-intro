from selenium import webdriver

chrome_driver_path = "/Users/nabil/Documents/code/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Opens a new Chrome window
driver.get("https://www.amazon.com")

# Closes the active tab
driver.close()

# Closes entire program
driver.quit()
