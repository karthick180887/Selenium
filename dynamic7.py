from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver service
service_obj = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Implicit wait
driver.implicitly_wait(5)

# Navigate to the URL
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

# Find the search input and type "ber"
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")

# Pause the test for 4 seconds
time.sleep(4)

# Find the number of products displayed
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3

# Click on all the add-to-cart buttons
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    button.click()

# Click on the cart icon
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

# Click on the proceed to checkout button using explicit wait
checkout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))
)
checkout_button.click()

# Enter the promo code
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")

# Click on the apply button using explicit wait
apply_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".promoBtn"))
)
apply_button.click()

# Wait for the promo information to be displayed
promo_info = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "span.promoInfo"))
)
print(promo_info.text)

# Close the browser
driver.quit()
