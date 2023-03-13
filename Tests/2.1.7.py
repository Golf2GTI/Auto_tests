from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_hidden = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_hidden.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robot_checkbox.click()

    robots_rule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots_rule.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button')
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()
