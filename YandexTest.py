from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'https://ya.ru/'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'найдётся всё']")
    input1.send_keys('Volkswagen Golf 2')
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()