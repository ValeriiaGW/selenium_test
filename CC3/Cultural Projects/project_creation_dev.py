import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import configuration
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


organization_name = "a_test_org"
cultural_project_name = "dev test deleting"


@pytest.fixture(scope="module")
def setup():
    browser = webdriver.Chrome()
    browser.get(url=configuration.BASE_URL_DEV)
    browser.find_element(
        by=By.CSS_SELECTOR,
        value=".input_input__l-JuX[name='username']") \
        .send_keys(configuration.admin_username)
    browser.find_element(
        by=By.CSS_SELECTOR,
        value=".input_input__l-JuX[name='password']") \
        .send_keys(configuration.admin_password)
    browser.find_element(by=By.CSS_SELECTOR, value=".button_children__2dy5b").click()
    # time.sleep(2)
    # current_url = browser.current_url
    # response = requests.get(current_url)
    # assert response.status_code == 200, f"Login failed, status code: {response.status_code}"
    yield browser
    browser.quit()


def test_creation_of_the_draft_project(setup):
    browser = setup
    wait = WebDriverWait(browser, 10)
    browser.find_element(by=By.XPATH, value=f"//div[contains(text(), '{organization_name}')]").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[descendant::div[text() = 'Create Culture Project']]")))
    browser.find_element(by=By.XPATH, value="//button[descendant::div[text() = 'Create Culture Project']]").click()

# Project title
    browser.find_element(by=By.CSS_SELECTOR, value=".styles_title-input__3ad9E").send_keys(f"{cultural_project_name}")

# Frequency
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#radio-button-frequency-1 span img")))
    browser.find_element(by=By.CSS_SELECTOR, value="#radio-button-frequency-1 span img").click()

# DATA SEGMENTATION GROUP 1
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-add-data-segmentation-group")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-data-segmentation-group").click()
    time.sleep(1)

# Data segmentation group - Title
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-data-segmentation-group")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-data-segmentation-group").send_keys(
        "Group question 1 Lorem ipsum dolor sit amet, conse")
    time.sleep(1)

# Data segmentation - Group survey question
    group_question_number = 1
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-survey-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-question").send_keys(
        f"Survey Question {group_question_number} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus non magna eget jk")
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-save-survey-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-survey-question").click()

# Data segmentation group - Segments
    for i in range(1, 9):
        if i < 8:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
                f"Segment {group_question_number}/{i} Lorem ipsum dolor sit ametoj fjabdfhkva")
            browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
            browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
        else:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
                f"Segment {group_question_number}/{i} Lorem ipsum dolor sit ametoj fjabdfhkva")
            browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
        i += 1

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-save-data-group-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-data-group-question").click()

# DATA SEGMENTATION GROUP 2
    group_question_number = 2
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-add-data-segmentation-group")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-data-segmentation-group").click()
    time.sleep(1)

# Data segmentation group - Title
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-data-segmentation-group")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-data-segmentation-group").send_keys(
        f"Group question {group_question_number} Lorem ipsum dolor sit amet, conse")
    time.sleep(1)

# Data segmentation - Group survey question

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-survey-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-question").send_keys(
        f"Survey Question {group_question_number} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus non magna eget jk")
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-save-survey-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-survey-question").click()


# Data segmentation group - Segments
    for i in range(1, 9):
        if i < 8:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
                f"Segment {group_question_number}/{i} Lorem ipsum dolor sit ametoj fjabdfhkva")
            browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
            browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
        else:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
                f"Segment {group_question_number}/{i} Lorem ipsum dolor sit ametoj fjabdfhkva")
            browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
        i += 1

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-save-data-group-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-data-group-question").click()


# KEY AREA 1

    key_area_number = 1
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-key-area").click()

    # Key area - title

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-key-area")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-key-area").send_keys(
        f"Key Area {key_area_number} Lorem ipsum dolor sit amet, consectetur")

    # Cultural pillar/Statement 1
    for i in range(1, 9):
        if i < 8:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
                f"CULTURAL PILLAR {key_area_number}/{i} Lorem ipsum dolor sit amet kjn")
            browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
                f"Statement {key_area_number}/{i} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")
            browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
        else:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
                f"CULTURAL PILLAR {key_area_number}/{i} Lorem ipsum dolor sit amet kjn")
            browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
                f"Statement {key_area_number}/{i} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

        i += 1

    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-key-area").click()

# KEY AREA 2

    key_area_number = 2
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-key-area").click()

    # Key area - title

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-key-area")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-key-area").send_keys(
        f"Key Area {key_area_number} Lorem ipsum dolor sit amet, consectetur")

    # Cultural pillar/Statement
    for i in range(1, 6):
        if i < 5:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
                f"CULTURAL PILLAR {key_area_number}/{i} Lorem ipsum dolor sit amet kjn")
            browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
                f"Statement {key_area_number}/{i} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")
            browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
        else:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
                f"CULTURAL PILLAR {key_area_number}/{i} Lorem ipsum dolor sit amet kjn")
            browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
                f"Statement {key_area_number}/{i} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

        i += 1

    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-key-area").click()

# KEY AREA 3

    key_area_number = 3
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-key-area").click()

    # Key area - title

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-key-area")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-key-area").send_keys(
        f"Key Area {key_area_number} Lorem ipsum dolor sit amet, consectetur")

    # Cultural pillar/Statement
    for i in range(1, 4):
        if i < 3:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
                f"CULTURAL PILLAR {key_area_number}/{i} Lorem ipsum dolor sit amet kjn")
            browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
                f"Statement {key_area_number}/{i} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")
            browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
        else:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
                f"CULTURAL PILLAR {key_area_number}/{i} Lorem ipsum dolor sit amet kjn")
            browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
                f"Statement {key_area_number}/{i} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

        i += 1

    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-key-area").click()

# KEY AREA 4

    key_area_number = 4
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-key-area").click()

    # Key area - title

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-key-area")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-key-area").send_keys(
        f"Key Area {key_area_number} Lorem ipsum dolor sit amet, consectetur")

    # Cultural pillar/Statement
    for i in range(1, 4):
        if i < 3:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
                f"CULTURAL PILLAR {key_area_number}/{i} Lorem ipsum dolor sit amet kjn")
            browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
                f"Statement {key_area_number}/{i} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")
            browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
        else:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
            browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
                f"CULTURAL PILLAR {key_area_number}/{i} Lorem ipsum dolor sit amet kjn")
            browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
                f"Statement {key_area_number}/{i} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

        i += 1

    browser.find_element(
        by=By.CSS_SELECTOR,
        value="#button-save-key-area").\
        click()


    browser.find_element(
        by=By.CSS_SELECTOR,
        value="#textarea-wordcloud-question").\
        send_keys(
        "The wordcloud question, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam lacinia quis lorem id tincidunt. Vestibulum erat massa, varius sit amet faucibus sed, gravida ac tortor")

    browser.find_element(by=By.CSS_SELECTOR, value=".styles_header__3Xygw #button-save-draft").click()

    current_url = browser.current_url

    projects_list = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".styles_title__37QYn")))
    projects_names = [project_name.text for project_name in projects_list]
    assert cultural_project_name in projects_names, f"Draft of cultural project with name {cultural_project_name} is not created"


    # time.sleep(3)
    # response = requests.post(current_url)
    # print(f"current_url = {current_url}")
    # print(f"response = {response}")
    # print(f"status_code = {response.status_code}")
    # assert response.status_code == 200, \
    #     f"Saving of the feedback framework as a draft failed, status code: {response.status_code}"