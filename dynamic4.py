from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://127.0.0.1:5000")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[name='data']").send_keys("Hi Karthick")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
time.sleep(2)
alert.accept()
time.sleep(2)
############################################333
driver.find_element(By.ID,"alertButton").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)
###################3
driver.find_element(By.ID,"confirmButton").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.dismiss()
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)
################
driver.find_element(By.ID,"modalButton").click()
time.sleep(2)
demo = driver.find_element(By.CSS_SELECTOR,"div[class='modal-content'] p").text
print(demo)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".close").click()
time.sleep(2)
driver.close()
