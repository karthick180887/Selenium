from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://127.0.0.1:5000")

dropdown = Select(driver.find_element(By.ID,"event_type"))
time.sleep(2)
dropdown.select_by_visible_text("concert")
time.sleep(2)
dropdown.select_by_visible_text("sports")

checkboxes = driver.find_elements(By.XPATH,"//input[@name='tickets']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "VIP Box":
        checkbox.click()
        # assert checkbox.is_selected()
        break

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
driver.close()

