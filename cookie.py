import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

store = driver.find_elements(By.CLASS_NAME, value="grayed")
item_ids = [item.get_attribute("id") for item in store]

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

timeout = time.time() + 5
five_min_later = time.time() + 300

while True:
    cookie.click()

    if time.time() > timeout:

        cookie_count = driver.find_element(By.ID, value="money")
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:

            if price.text != "":

                item_cost = int(price.text.split(" - ")[1].replace(",", ""))
                item_prices.append(item_cost)

        cookie_count = int(cookie_count.text)
        cookie_upgrades = {}

        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        affordable_upgrades = {}

        for (cost, id) in cookie_upgrades.items():

            if cookie_count > cost:

                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

        if time.time() > five_min_later:
            cps = driver.find_element(By.ID, value='cps')
            print(cps.text)
            break



