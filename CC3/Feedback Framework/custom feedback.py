import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://cultural-calculator-frontend-stage.s3-website.eu-west-2.amazonaws.com/feedback-process/aed1b208-bd96-46d8-8738-7da757fa7ac1"  #change
role = "Self"                                                                                     #change
round_number = 1                                                                                      #change
res = []
try:
    browser.get(link)
    browser.implicitly_wait(1)

    check_box = browser.find_element(by=By.CSS_SELECTOR, value='[data-test="checkbox"]')
    check_box.click()

    get_started_btn = browser.find_element(by=By.CSS_SELECTOR, value='[type="button"]')
    get_started_btn.click()
    count = 1
    # text = {
    #     'short': "lorem",
    #     "long": "Lorem ipsum dolor sit amet, consecо" * 10
    # }
    colour_list = [
        {
            'color': "44, 42, 67",
            'value': 1
        },
        {
            "color": "55, 65, 104",
            "value": 2
        },
        {
            "color": "66, 87, 141",
            "value": 3
        },
        {
            "color": "78, 111, 179",
            "value": 4
        },
        {
            "color": "89, 133, 216",
            "value": 5
        },
        {
            "color": "101, 157, 254",
            "value": 6
        },
        {
            "color": "109, 177, 249",
            "value": 7
        },
        {
            "color": "117, 196, 245",
            "value": 8
        },
        {
            "color": "124, 216, 242",
            "value": 9
        },
        {
            "color": "132, 235, 238",
            "value": 10
        }

    ]
    while True:
        try:
            colors = []
            for i in range(8):
                random_color = random.choice(colour_list)
                browser.find_element(
                    by=By.CSS_SELECTOR,
                    value=f'[data-test="qualities-evaluate-{i}"] [style="background-color: '
                          f'rgb({random_color["color"]});"]').click()
                colors.append(random_color["value"])
                browser.find_element(
                    by=By.CSS_SELECTOR,
                    value='[data-test="question-textarea-1"]').send_keys(
                    # text["short"] if count % 2 == 0 else text["long"]
                    f'Question 1, {role}, round - {round_number} '
                )
                browser.find_element(
                    by=By.CSS_SELECTOR,
                    value='[data-test="question-textarea-2"]').send_keys(
                    # text["long"] if count % 2 == 0 else text["short"]
                    f'Question 2, {role}, round - {round_number} '
                )

                count += 1
            res.append(colors)
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

    for item in res:
        print(item)

    # with open("testrounds_reminder.csv", "a") as file:                                                     #file name
    #     for item in res:
    #         file.write(role + str(item) + "\n")

    confirm_btn = browser.find_element(by=By.CSS_SELECTOR, value='[data-test="button-confirm-send"]')
    confirm_btn.click()


finally:
    time.sleep(5)
    browser.quit()
