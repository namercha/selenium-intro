from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/nabil/Documents/code/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Opens a new Chrome window
# driver.get("https://www.amazon.com")

# Previous project "price-tracker" done with Selenium
# driver.get("https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_fod_2?pd_rd_i"
#            "=B08PPZWNCV&th=1")
# price = driver.find_element(id, "a-offscreen")
# print(price.text)


# Useful when filling out web forms
driver.get("https://python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar)
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
#
# documentation_link = driver.find_element_by_css_selector(".documentation_widget a")
# print(documentation_link.text)
#
# # Getting the "Submit Bug link on bottom of page bysing Xpath
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
#
# # Getting multiple elements
# driver.find_elements_by_css_selector()

# Getting a list of upcoming events from the python.org website and saving them in a dictionary
event_times = driver.find_elements_by_css_selector(".event_widget time")
event_names = driver.find_element(By.CSS_SELECTOR, ".event_widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n],
        "name": event_names[n]
    }

print(events)

# Closes the active tab
# driver.close()

# Closes entire program
driver.quit()
