from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.implicitly_wait(2)
browser.get("https://demoqa.com/dynamic-properties")
wait = WebDriverWait(browser, 15, poll_frequency=1)

BUTTON = ("xpath", "//button[@id='colorChange']")
wait.until(EC.visibility_of_element_located(BUTTON)).click()
time.sleep(5)

print("Прошло успешно!")