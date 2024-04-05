from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events_dic = {

}
for event in events:
    event_dic = {
        "time": event.text.split()[0],
        "name": event.text.split()[1] + " " + event.text.split()[2] + " " + event.text.split()[3],
    }
    for i in range(0, 5):
        events_dic[i] = event_dic
print(events_dic)


