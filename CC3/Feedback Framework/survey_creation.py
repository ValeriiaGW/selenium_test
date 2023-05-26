import random
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import Configuration
from Configuration import BASE_URL_DEV

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

try:
    browser.get(Configuration.BASE_URL_DEV)
    browser.find_element(
        by=By.CSS_SELECTOR,
        value="#root > div > div > div > div > form > div.auth_form-group__UzVsX > div:nth-child(1) > div > input")\
        .send_keys("valeriia.b@gowombat.team")
    browser.find_element(
        by=By.CSS_SELECTOR,
        value="#root > div > div > div > div > form > div.auth_form-group__UzVsX > div:nth-child(2) > div > input")\
        .send_keys("Qwerty123!")
    browser.find_element(by=By.CSS_SELECTOR, value=".button_children__2dy5b").click()
    time.sleep(2)

# # creation of the organization

    # browser.find_element(
    #     by=By.CSS_SELECTOR,
    #     value="#root > div > div > div:nth-child(2) > div > div > div:nth-child(3) > div.styles_container__L645k.styles_area__1Aju_ > button")\
    #     .click()
    # browser.find_element(by=By.CSS_SELECTOR, value=".styles_input__3_DsR").send_keys("test_org")
    # browser.find_element(
    #     by=By.CSS_SELECTOR,
    #     value="#root > div > div > div:nth-child(2) > div > div > div:nth-child(3) > form > div.styles_button-group__1pGSQ > button.button_button__14uPl.button_primary__1JMvQ.styles_button__23gPD.btn.btn-primary")\
    #     .click()
    browser.find_element(by=By.XPATH, value="//div[contains(text(), 'test_org')]").click()

# Cultural project creation

    browser.find_element(by=By.XPATH, value="//button[descendant::div[text() = 'Create Culture Project']]").click()

# Project title

    browser.find_element(by=By.CSS_SELECTOR, value=".styles_title-input__3ad9E").send_keys(
        "Test 1")

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

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-survey-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-question").send_keys(
        "Survey Question 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus non magna eget jk")
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-save-survey-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-survey-question").click()

    # Data segmentation group - Segments

    # 1
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment").send_keys(
        "Segment 1/1 Lorem ipsum dolor sit ametoj fjabdfhkva")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 2
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 1/2 Lorem ipsum dolor sit ametoj djabdfhkva")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 3
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 1/3 Lorem ipsum dolor sit ametoj sjabdfhkva")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 4
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 1/4 Lorem ipsum dolor sit ametoj gjabdfhkva")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 5
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 1/5 Lorem ipsum dolor sit ametoj hjabdfhkva")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 6
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 1/6 Lorem ipsum dolor sit ametoj  jabdfhkva")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 7
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 1/7 Lorem ipsum dolor sit ametoj  jabdfhkva")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 8
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 1/8 Lorem ipsum dolor sit ametoj  jabdfhkva")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()

    #  Save

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-save-data-group-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-data-group-question").click()

# DATA SEGMENTATION GROUP 2

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-add-data-segmentation-group")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-data-segmentation-group").click()
    time.sleep(1)

    # Data segmentation group - Title

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-data-segmentation-group")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-data-segmentation-group").send_keys(
        "Group question 2")
    time.sleep(1)

    # Data segmentation - Group survey question

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-survey-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-question").send_keys(
        "Survey Question 2")
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-save-survey-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-survey-question").click()

    # Data segmentation group - Segments

    # 1
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment").send_keys(
        "Segment 2/1 Lorem ipsum")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 2
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 2/2 Lorem ipsum dolor")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 3
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 2/3 Lorem ipsum dolor sit ametoj")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 4
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 2/4 Lorem")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 5
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 2/5 Lorem ipsum")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 6
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 2/6 Lorem ipsum dol")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 7
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 2/7 Lorem ipsum")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()
    # 8
    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-segment").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-segment:not([disabled])")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-segment:not([disabled])").send_keys(
        "Segment 2/8")
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-segment").click()

    #  Save

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-save-data-group-question")))
    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-data-group-question").click()


# KEY AREA 1

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-key-area").click()
    # Key area - title
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-key-area")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-key-area").send_keys(
        "Key Area 1 Lorem ipsum dolor sit amet, consectetur")

    # Cultural pillar/Statement 1

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 1/1 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 1/1 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 2

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 1/2 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 1/2 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 3

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 1/3 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 1/3 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 4

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 1/4 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 1/4 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 5

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 1/5 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 1/5 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 6

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 1/6 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 1/6 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 7

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 1/7 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 1/7 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 8

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 1/8 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 1/8 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # save

    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-key-area").click()

# KEY AREA 2

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-key-area").click()
    # Key area - title
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-key-area")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-key-area").send_keys(
        "Key Area 2 Lorem ipsum dolor sit amet, consectetur")

    # Cultural pillar/Statement 1

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 2/1 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 2/1")

    # Cultural pillar/Statement 2

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 2/2 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 2/2")

    # Cultural pillar/Statement 3

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 2/3 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 2/3")

    # Cultural pillar/Statement 4

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 2/4 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 2/4")

    # Cultural pillar/Statement 5

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 2/5 Lorem ipsum dolor sit amet kjn")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 2/5")


    # save

    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-key-area").click()

# KEY AREA 3

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-key-area").click()
    # Key area - title
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-key-area")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-key-area").send_keys(
        "Key Area 3 Lorem ipsum dolor sit amet, consectetur")

    # Cultural pillar/Statement 1

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 3/1")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 3/1 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 2

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 3/2")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 3/2 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 3

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 3/3")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 3/3 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # save

    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-key-area").click()

# KEY AREA 4

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-key-area").click()
    # Key area - title
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-name-key-area")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-name-key-area").send_keys(
        "Key Area 4 Lorem ipsum dolor sit amet, consectetur")

    # Cultural pillar/Statement 1

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-cultural-pillar[value='']")))
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 3/1")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 3/1 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 2

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 3/2")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 3/2 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # Cultural pillar/Statement 3

    browser.find_element(by=By.CSS_SELECTOR, value="#button-add-survey-statement").click()
    browser.find_element(by=By.CSS_SELECTOR, value="#input-cultural-pillar[value='']").send_keys(
        "CULTURAL PILLAR 3/3")
    browser.find_element(by=By.CSS_SELECTOR, value="#input-survey-statement[value='']").send_keys(
        "Statement 3/3 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet leo non ante tincidunt blandijkbkj")

    # save

    browser.find_element(by=By.CSS_SELECTOR, value="#button-save-key-area").click()


    browser.find_element(by=By.CSS_SELECTOR, value="#textarea-wordcloud-question").send_keys(
        "The wordcloud question, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam lacinia quis lorem id tincidunt. Vestibulum erat massa, varius sit amet faucibus sed, gravida ac tortor")


    browser.find_element(by=By.CSS_SELECTOR, value=".styles_header__3Xygw #button-save-draft").click()


except NoSuchElementException:
    pass


finally:
    time.sleep(5)
    browser.quit()