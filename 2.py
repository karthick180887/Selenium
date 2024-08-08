import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com")
time.sleep(20)