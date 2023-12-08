import pytest
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import configuration
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

wordcloud_text = "cat car red in an all yep role test i me my myself we our youre youve youll youd your mustnt needn neednt shan shant shouldn yours yourself yourselves ours ourselves you he herself it its its itself they them their theirs themselves what him his himself she am is are was were be been being have has had having do does did doing a shes her hers which who whom this that thatll these those an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don dont should shouldve now d ll m o re ve y ain aren arent couldn mightnt mustn shouldnt wasn wasnt weren werent couldnt didn didnt doesn doesnt hadn hadnt hasn hasnt haven havent isn isnt ma mightn won wont wouldn wouldnt stop words"

r_buttons_group = [
    "#radio-button-0 .styles_checkmark__2ORUe",
    "#radio-button-1 .styles_checkmark__2ORUe",
    "#radio-button-2 .styles_checkmark__2ORUe",
    "#radio-button-3 .styles_checkmark__2ORUe",
    "#radio-button-4 .styles_checkmark__2ORUe",
    "#radio-button-5 .styles_checkmark__2ORUe",
    "#radio-button-6 .styles_checkmark__2ORUe",
    "#radio-button-7 .styles_checkmark__2ORUe",
    "#radio-button-8 .styles_checkmark__2ORUe",
    "#radio-button-9 .styles_checkmark__2ORUe"
]


colour_list = [
    "button-evaluation-1",
    "button-evaluation-2",
    "button-evaluation-3",
    "button-evaluation-4",
    "button-evaluation-5",
    "button-evaluation-6",
    "button-evaluation-7"
]
survey_links = configuration.email_list

def random_group(setup):
    browser = setup
    while r_buttons_group:
        random_colour = random.choice(r_buttons_group)
        try:
            browser.find_element(by=By.CSS_SELECTOR, value=f"{random_colour}").click()
            # time.sleep(2)
            print(random_colour, 1)
            return
        except:
            r_buttons_group.remove(random_colour)
            print(r_buttons_group, 1)


def random_key_area_color(setup):
    browser = setup
    count = 1
    try:
        for i in range(8):
            random_colour = random.choice(colour_list)
            browser.find_element(
                by=By.CSS_SELECTOR,
                value=f'#question-evaluation-box-{i} #{random_colour}'
            ).click()
            count += 1

    except NoSuchElementException:
        pass


@pytest.fixture(scope="module")
def setup(request):
    link = request.param
    browser = webdriver.Chrome()
    browser.get(url=link)
    yield browser
    browser.quit()


@pytest.mark.parametrize("setup", survey_links, indirect=True)
def test_survey_submitting(setup):
    browser = setup
    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#button-get-started")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-get-started").click()
    # time.sleep(2)

    try:
        count = 1
        for i in range(5):
            random_group(setup)
            browser.find_element(by=By.CSS_SELECTOR, value="#button-next").click()
            count += 1

    except NoSuchElementException:
        pass

    try:
        count = 1
        for i in range(4):
            random_key_area_color(setup)
            # time.sleep(2)
            browser.find_element(by=By.CSS_SELECTOR, value="#button-next").click()
            count += 1
    except NoSuchElementException:
        pass

    browser.find_element(
        by=By.CSS_SELECTOR,
        value='#input-wordcloud-answer'
    ).send_keys(wordcloud_text)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-finish")))

    browser.find_element(by=By.CSS_SELECTOR, value='#button-finish').click()

    time.sleep(1)

    final_text = browser.find_element(
        by=By.CSS_SELECTOR,
        value='[class = "styles_info-block__XFd-7 styles_thank-you-block__3Pyk1"]'
    ).text

    assert final_text == "Thank you for sharing your experience!", f'{final_text} is displayed'


time.sleep(3)
