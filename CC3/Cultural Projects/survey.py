import random
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


browser = webdriver.Chrome()

stage = "stage.culturalcalculator.co.uk"
dev = "devs.culturalcalculator.co.uk"

participant_id = "9daba5e5-0bac-4e27-88e8-015b79cf86a8"

# link = f"https://{dev}/cultural-project-process/{participant_id}"

link = "https://culturalcalculator.co.uk/cultural-project-process/d46c5858-5961-4300-a903-2a2ecae1c3ca"

wordcloud_text = "test "

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
survey_result = []

try:
    browser.get(link)
    browser.implicitly_wait(1)
    # survey start
    browser.find_element(by=By.CSS_SELECTOR, value="#button-get-started").click()
    group_values = []

    try:
        # first question
        browser.find_element(
            by=By.CSS_SELECTOR,
            value=f'{random_button_group_1}'
        ).click()
        group_values.append(random_button_group_1)

        browser.find_element(
            by=By.CSS_SELECTOR,
            value='#button-next'
        ).click()

        # second question
        browser.find_element(
            by=By.CSS_SELECTOR,
            value=f'{random_button_group_2}'
        ).click()
        group_values.append(random_button_group_2)

        browser.find_element(
            by=By.CSS_SELECTOR,
            value='#button-next'
        ).click()

        # third question

        key_values_3 = []

        for i in range(8):
            random_colour = random.choice(colour_list)
            browser.find_element(
                by=By.CSS_SELECTOR,
                value=f'#question-evaluation-box-{i} #{random_colour["colour"]}'
            ).click()
            count += 1
            key_values_3.append({random_colour['value']})

        browser.find_element(
            by=By.CSS_SELECTOR,
            value='#button-next'
        ).click()

        # fourth question

        key_values_4 = []

        for i in range(5):
            random_colour = random.choice(colour_list)
            browser.find_element(
                by=By.CSS_SELECTOR,
                value=f'#question-evaluation-box-{i} #{random_colour["colour"]}'
            ).click()
            count += 1
            key_values_4.append({random_colour['value']})

        browser.find_element(
            by=By.CSS_SELECTOR,
            value='#button-next'
        ).click()

        # fifth question

        key_values_5 = []

        for i in range(3):
            random_colour = random.choice(colour_list)
            browser.find_element(
                by=By.CSS_SELECTOR,
                value=f'#question-evaluation-box-{i} #{random_colour["colour"]}'
            ).click()
            count += 1
            key_values_5.append({random_colour['value']})

        browser.find_element(
            by=By.CSS_SELECTOR,
            value='#button-next'
        ).click()

        # sixth question

        key_values_6 = []

        for i in range(3):
            random_colour = random.choice(colour_list)
            browser.find_element(
                by=By.CSS_SELECTOR,
                value=f'#question-evaluation-box-{i} #{random_colour["colour"]}'
            ).click()
            count += 1
            key_values_6.append({random_colour['value']})

        browser.find_element(
            by=By.CSS_SELECTOR,
            value='#button-next'
        ).click()

        # seventh question Wordcloud

        browser.find_element(
            by=By.CSS_SELECTOR,
            value='#input-wordcloud-answer'
        ).send_keys(wordcloud_text)

        browser.find_element(by=By.CSS_SELECTOR, value='#button-finish').click()

        time.sleep(1)

        final_text = browser.find_element(
            by=By.CSS_SELECTOR,
            value='[class = "styles_info-block__XFd-7 styles_thank-you-block__3Pyk1"]'
        ).text


        def test_final_text():
            assert final_text == "Thank you for sharing your experience!", f'{final_text} is displayed'

        survey_result.append(group_values + key_values_3 + key_values_4 + key_values_5 + key_values_6)

        # with open("notif 4 weeks", 'a') as file:                       # file name
        #     for item in survey_result:
        #         file.write(participant + str(item) + "\n")

        # final_text = browser.find_element(
        #     by=By.CSS_SELECTOR,
        #     value='[class = "styles_info-block__XFd-7 styles_thank-you-block__3Pyk1"]'
        # )

    except NoSuchElementException:
        pass

except NoSuchElementException:
    pass

finally:

    time.sleep(5)
    browser.quit()

# try:
#     browser.get(link)
#     browser.implicitly_wait(1)
#     final_text_2 = browser.find_element(
#         by=By.CSS_SELECTOR,
#         value='.styles_info-block__XFd-7 > .styles_title__15uBx'
#     ).text
#
#
#     def test_second_attempt_to_pass_survey():
#         assert final_text_2 == "Thanks for checking in but you have already submitted your survey for this round!", \
#             f'{final_text_2} is displayed'
#
# except NoSuchElementException:
#     pass
#
# finally:
#     time.sleep(3)
#     browser.quit()





