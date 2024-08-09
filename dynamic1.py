from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
# "li[class='ui-menu-item'] a"
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        time.sleep(2)
        break

# print(driver.find_element(By.ID, "autosuggest").text) -> static Value
# print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) - Dynamic Value
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
driver.close()
