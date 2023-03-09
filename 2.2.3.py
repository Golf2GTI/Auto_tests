from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = (browser.find_element(By.CSS_SELECTOR, '#num1'))
    y = (browser.find_element(By.CSS_SELECTOR, '#num2'))
    num1 = int(x.text)
    num2 = int(y.text)
    f = str(num1+num2)





    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(f)

    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(5)
    browser.quit()


