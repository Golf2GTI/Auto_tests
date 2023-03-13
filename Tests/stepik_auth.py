from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
def test_auth(browser):
    browser.get('https://stepik.org/lesson/236895/step/1')
    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, 'ember33'))
    )
    browser.find_element(By.CSS_SELECTOR, '#ember33').click()
    browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys('email')
    browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys('password')
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, 'ember34'))
    )



