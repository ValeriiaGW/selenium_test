import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://devs.culturalcalculator.co.uk/cultural-project-process/f4a305f1-70d8-478b-a1f3-e79f3b2410ad/?project_id=ba1e49a2-dba0-4a71-a111-eb594c091faf"

r_buttons_group_1 = ["#radio-button-0 .styles_checkmark__2ORUe",
                     "#radio-button-1 .styles_checkmark__2ORUe",
                     "#radio-button-2 .styles_checkmark__2ORUe",
                     "#radio-button-3 .styles_checkmark__2ORUe",
                     "#radio-button-4 .styles_checkmark__2ORUe",
                     "#radio-button-5 .styles_checkmark__2ORUe",
                     "#radio-button-6 .styles_checkmark__2ORUe",
                     "#radio-button-7 .styles_checkmark__2ORUe",
                     "#radio-button-8 .styles_checkmark__2ORUe"]

random_button_group_1 = random.choice(r_buttons_group_1)

r_buttons_group_2 = ["#radio-button-0 .styles_checkmark__2ORUe",
                     "#radio-button-1 .styles_checkmark__2ORUe"]
random_button_group_2 = random.choice(r_buttons_group_2)
colour_list = [
    {
        "colour": "button-evaluation-1",
        "value": 1
    },
    {
        "colour": "button-evaluation-2",
        "value": 2
    },
    {
        "colour": "button-evaluation-3",
        "value": 3
    },
    {
        "colour": "button-evaluation-4",
        "value": 4
    },
    {
        "colour": "button-evaluation-5",
        "value": 5
    },
    {
        "colour": "button-evaluation-6",
        "value": 6
    },
    {
        "colour": "button-evaluation-7",
        "value": 7
    }]

count = 1
try:
    browser.get(link)
    browser.implicitly_wait(1)
    # survey start
    browser.find_element(by=By.CSS_SELECTOR, value="#button-get-started").click()

# first question
    for i in range(9):
        browser.find_element(
            by=By.CSS_SELECTOR,
            value=f'#radio-button-{i} .styles_checkmark__2ORUe'
        ).click()

    browser.find_element(
        by=By.CSS_SELECTOR,
        value='#button-next'
    ).click()

# second question
    for i in range(5):
        browser.find_element(
            by=By.CSS_SELECTOR,
            value=f'#radio-button-{i} .styles_checkmark__2ORUe'
        ).click()

    browser.find_element(
        by=By.CSS_SELECTOR,
        value='#button-next'
    ).click()

# third question

    for i in range(8):
        random_colour = random.choice(colour_list)
        browser.find_element(
            by=By.CSS_SELECTOR,
            value=f'#question-evaluation-box-{i} #{random_colour["colour"]}'
        ).click()
        count += 1

    browser.find_element(
        by=By.CSS_SELECTOR,
        value='#button-next'
    ).click()

# fourth question

    for i in range(5):
        random_colour = random.choice(colour_list)
        browser.find_element(
            by=By.CSS_SELECTOR,
            value=f'#question-evaluation-box-{i} #{random_colour["colour"]}'
        ).click()
        count += 1

    browser.find_element(
        by=By.CSS_SELECTOR,
        value='#button-next'
    ).click()

# fifth question

    for i in range(3):
        random_colour = random.choice(colour_list)
        browser.find_element(
            by=By.CSS_SELECTOR,
            value=f'#question-evaluation-box-{i} #{random_colour["colour"]}'
        ).click()
        count += 1

    browser.find_element(
        by=By.CSS_SELECTOR,
        value='#button-next'
    ).click()

# sixth question

    for i in range(3):
        random_colour = random.choice(colour_list)
        browser.find_element(
            by=By.CSS_SELECTOR,
            value=f'#question-evaluation-box-{i} #{random_colour["colour"]}'
        ).click()
        count += 1

    browser.find_element(
        by=By.CSS_SELECTOR,
        value='#button-next'
    ).click()

# seventh question

    browser.find_element(by=By.CSS_SELECTOR, value='#input-wordcloud-answer').send_keys("test first ")
    browser.find_element(by=By.CSS_SELECTOR, value='#button-finish').click()

    final_text = browser.find_element(
        by=By.CSS_SELECTOR,
        value='[class = "styles_info-block__XFd-7 styles_thank-you-block__3Pyk1"]'
    )
    final_text_text = final_text.text
    assert "Thank you for sharing your experience!" == final_text_text, f'{final_text_text} is displayed'

finally:

    time.sleep(5)
    browser.quit()
