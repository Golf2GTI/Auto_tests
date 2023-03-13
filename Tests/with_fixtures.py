from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import pytest

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    yield browser
    browser.quit()

def test1(browser):
    # link = 'http://suninjuly.github.io/redirect_accept.html'
    # browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

