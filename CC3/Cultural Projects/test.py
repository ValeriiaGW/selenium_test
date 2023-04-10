from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
link = "https://devs.culturalcalculator.co.uk/"

try:
    browser.get(link)
    browser.implicitly_wait(1)

    browser.find_element(
        by=By.XPATH,
        value='//*[@id="root"]/div/div/div/div/form/div[1]/div[1]/div/input').\
        send_keys("valeriia.b@gowombat.team")
    browser.find_element(
        by=By.XPATH,
        value='//*[@id="root"]/div/div/div/div/form/div[1]/div[2]/div/input').\
        send_keys("Qwerty123!")
    browser.find_element(
        by=By.XPATH,
        value='//*[@id="root"]/div/div/div/div/form/div[3]/button').\
        click()

    # organization = browser.find_element(by=By.CSS_SELECTOR, value='[Test Projects]')

finally:
    time.sleep(5)
    browser.quit()
