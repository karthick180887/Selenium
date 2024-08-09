from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://127.0.0.1:5000")

dropdown = Select(driver.find_element(By.ID,"shows"))
time.sleep(2)
dropdown.select_by_visible_text("Movie B")
time.sleep(2)

radiobuttons = driver.find_elements(By.CSS_SELECTOR,"input[name='timing']")
print(len(radiobuttons))
for radio in radiobuttons:
    if radio.get_attribute("value") == "11:00 AM":
        radio.click()
        break
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.close()