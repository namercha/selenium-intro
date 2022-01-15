from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.common.exceptions import StaleElementReferenceException

URL = "http://orteil.dashnet.org/experiments/cookie/"
PLAYTIME = 5

chrome_driver_path = "/Users/nabil/Documents/code/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

clicker = driver.find_element(By.ID, "cookie")
all_products = driver.find_element(By.CLASS_NAME, "grayed")
product_data = [product.text.split("\n")[0] for product in all_products]

product_dict = {product.split(" -")[0]: int(product.split(" - ")[1].replace(",", "")) for product in product_data if
                len(product) != 0}

timeout = datetime.now() + timedelta(minutes=PLAYTIME)


def check_product():
    global product_dict
    cookies_num = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    expensive_product = None
    for value, key in product_dict.items():
        if cookies_num > key:
            expensive_product = value
    if expensive_product is not None:
        try:
            buy_button = driver.find_element(By.ID, "store").find_element(By.CSS_SELECTOR, f"#buy{expensive_product}")
            buy_button.click()
            product_dict = {product.split(" -")[0]: int(product.split(" - ")[1].replace(",", "")) for product in
                            product_data if
                            len(product) != 0}
        except StaleElementReferenceException as e:
            print(f"Exception found: {e}")
            pass


while datetime.now() < timeout:
    clicker.click()
    now_secs = int(datetime.now().strftime("%S"))
    if now_secs % 8 == 0:
        check_product()

speed = driver.find_element(By.ID, "cps").text
print(f"Cookies/second: {speed}")
driver.quit()
