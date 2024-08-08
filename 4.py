from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Selenium supports several locators to find elements on a webpage.
# ID, Name, Class Name, Tag Name, Link Text, Partial Link Text, CSS Selector, XPath

driver.find_element(By.NAME,"name").send_keys("Karthick Selvam")
driver.find_element(By.NAME,"email").send_keys("karthick123@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("password")
driver.find_element(By.ID,"exampleCheck1").click()

#XPATH = //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH,"//input[@type='submit']").click()

#CSS = tagname[attribute='value'] -> input[name='name']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("New Name")

message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)

#Assertion will do validitatio for exact text
assert "Success" in message
driver.close()
#exampleFormControlSelect1