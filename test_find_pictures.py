from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
PICTURES_BUTTON = (By.XPATH, '//*[@aria-label="Поиск картинок (откроется новая вкладка)"]')
FIND_TEXT = (By.XPATH, '//*[text()="Картинки"]')

def find_element(driver, locator, time=5):
    return WebDriverWait(driver, time).until(EC.presence_of_element_located(locator))

def test_error_auth():
    driver.get("http://google.com")
    find_element(driver, PICTURES_BUTTON).click()
    find_element(driver, FIND_TEXT)