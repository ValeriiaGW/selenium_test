import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("https://devs.culturalcalculator.co.uk/feedback-process/0b285210-4f39-4ec4-9119-c62de009c472")
    browser.implicitly_wait(1)

    check_box = browser.find_element(by=By.CSS_SELECTOR, value='[data-test="checkbox"]')
    check_box.click()

    get_started_btn = browser.find_element(by=By.CSS_SELECTOR, value='[type="button"]')
    get_started_btn.click()

    while True:
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="qualities-evaluate-0"] [style="background-color: rgb(55, 65, 104);"]').click()
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="qualities-evaluate-1"] [style="background-color: rgb(124, 216, 242);"]').click()
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="qualities-evaluate-2"] [style="background-color: rgb(101, 157, 254);"]').click()
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="qualities-evaluate-3"] [style="background-color: rgb(101, 157, 254);"]').click()
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="qualities-evaluate-4"] [style="background-color: rgb(101, 157, 254);"]').click()
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="qualities-evaluate-5"] [style="background-color: rgb(101, 157, 254);"]').click()
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="qualities-evaluate-6"] [style="background-color: rgb(101, 157, 254);"]').click()
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="qualities-evaluate-7"] [style="background-color: rgb(101, 157, 254);"]').click()
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="question-textarea-1"]').send_keys("Lorem Ipsum 1")
        browser.find_element(by=By.CSS_SELECTOR, value='[data-test="question-textarea-2"]').send_keys("Lorem Ipsum 2")

        try:
            submit_btn = browser.find_element(by=By.CSS_SELECTOR, value='[data-test="button-confirm"]')
        except NoSuchElementException:
            pass
        else:
            submit_btn.click()
            break

        next_btn = browser.find_element(by=By.CSS_SELECTOR, value='[data-test="button-next"]')
        next_btn.click()

    confirm_btn = browser.find_element(by=By.CSS_SELECTOR, value='[data-test="button-confirm-send"]')
    confirm_btn.click()


finally:
    time.sleep(5)
    browser.quit()

# buttons

# style="background-color: rgb(44, 42, 67);"
# style="background-color: rgb(55, 65, 104);"

# style="background-color: rgb(66, 87, 141);"
# style="background-color: rgb(78, 111, 179);"

# style="background-color: rgb(89, 133, 216);"
# style="background-color: rgb(101, 157, 254);"

# style="background-color: rgb(109, 177, 249);"
# style="background-color: rgb(117, 196, 245);"

# style="background-color: rgb(124, 216, 242);"
# style="background-color: rgb(132, 235, 238);"