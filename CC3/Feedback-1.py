import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://devs.culturalcalculator.co.uk/feedback-process/60b88ff3-7784-4ad4-8b3b-1bca753b5416"
try:
    browser.get(link)
    browser.implicitly_wait(1)

    check_box = browser.find_element(by=By.CSS_SELECTOR, value='[data-test="checkbox"]')
    check_box.click()

    get_started_btn = browser.find_element(by=By.CSS_SELECTOR, value='[type="button"]')
    get_started_btn.click()
    count = 1
    text = {
        'short': "lorem",
        "long": "Lorem ipsum dolor sit amet, consecо" * 10
    }
    colour_list = [
        "44, 42, 67",
        "55, 65, 104",
        "66, 87, 141",
        "78, 111, 179",
        "89, 133, 216",
        "101, 157, 254",
        "109, 177, 249",
        "117, 196, 245",
        "124, 216, 242",
        "132, 235, 238"
    ]

    while True:
        try:
            for i in range(8):
                browser.find_element(
                    by=By.CSS_SELECTOR,
                    value=f'[data-test="qualities-evaluate-{i}"] [style="background-color: '
                          f'rgb({random.choice(colour_list)});"]').click()
            # browser.find_element(
            #     by=By.CSS_SELECTOR,
            #     value=f'[data-test="qualities-evaluate-1"] [style="background-color: '
            #           f'rgb({random.choice(colour_list)});"]').click()
            # browser.find_element(
            #     by=By.CSS_SELECTOR,
            #     value=f'[data-test="qualities-evaluate-2"] [style="background-color: '
            #           f'rgb({random.choice(colour_list)});"]').click()
            # browser.find_element(
            #     by=By.CSS_SELECTOR,
            #     value=f'[data-test="qualities-evaluate-3"] [style="background-color: '
            #           f'rgb({random.choice(colour_list)});"]').click()
            # browser.find_element(
            #     by=By.CSS_SELECTOR,
            #     value=f'[data-test="qualities-evaluate-4"] [style="background-color: '
            #           f'rgb({random.choice(colour_list)});"]').click()
            # browser.find_element(
            #     by=By.CSS_SELECTOR,
            #     value=f'[data-test="qualities-evaluate-5"] [style="background-color: '
            #           f'rgb({random.choice(colour_list)});"]').click()
            # browser.find_element(
            #     by=By.CSS_SELECTOR,
            #     value=f'[data-test="qualities-evaluate-6"] [style="background-color: '
            #           f'rgb({random.choice(colour_list)});"]').click()
            # browser.find_element(
            #     by=By.CSS_SELECTOR,
            #     value=f'[data-test="qualities-evaluate-7"] [style="background-color: '
            #           f'rgb({random.choice(colour_list)});"]').click()
                browser.find_element(
                    by=By.CSS_SELECTOR,
                    value='[data-test="question-textarea-1"]').send_keys(
                    text["short"] if count % 2 == 0 else text["long"]
                )
                browser.find_element(
                    by=By.CSS_SELECTOR,
                    value='[data-test="question-textarea-2"]').send_keys(
                    text["long"] if count % 2 == 0 else text["short"]
                )
                count += 1

        except NoSuchElementException:
            continue

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
