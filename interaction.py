from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
f_name.send_keys("Rafet", Keys.ENTER)

l_name = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
l_name.send_keys("31", Keys.ENTER)

email = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
email.send_keys("rafetcode@gmail.com", Keys.ENTER)







