import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def feedback_process(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    check_box = browser.find_element(by=By.CSS_SELECTOR, value='[data-test="checkbox"]')
    check_box.click()

    get_started_btn = browser.find_element(by=By.CSS_SELECTOR, value='[type="button"]')
    get_started_btn.click()

    while True:
        browser.find_element(
            by=By.CSS_SELECTOR,
            value='[data-test="qualities-evaluate-0"] [style="background-color: rgb(55, 65, 104);"]')\
            .click()
        browser.find_element(
            by=By.CSS_SELECTOR,
            value='[data-test="qualities-evaluate-1"] [style="background-color: rgb(124, 216, 242);"]')\
            .click()
        browser.find_element(
            by=By.CSS_SELECTOR,
            value='[data-test="qualities-evaluate-2"] [style="background-color: rgb(101, 157, 254);"]')\
            .click()
        browser.find_element(
            by=By.CSS_SELECTOR,
            value='[data-test="qualities-evaluate-3"] [style="background-color: rgb(101, 157, 254);"]')\
            .click()
        browser.find_element(
            by=By.CSS_SELECTOR,
            value='[data-test="qualities-evaluate-4"] [style="background-color: rgb(101, 157, 254);"]')\
            .click()
        browser.find_element(
            by=By.CSS_SELECTOR,
            value='[data-test="qualities-evaluate-5"] [style="background-color: rgb(101, 157, 254);"]')\
            .click()
        browser.find_element(
            by=By.CSS_SELECTOR,
            value='[data-test="qualities-evaluate-6"] [style="background-color: rgb(101, 157, 254);"]')\
            .click()
        browser.find_element(
            by=By.CSS_SELECTOR,
            value='[data-test="qualities-evaluate-7"] [style="background-color: rgb(101, 157, 254);"]')\
            .click()
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

    finish_text = browser.find_element(by=By.CSS_SELECTOR, value=".styles_text__O2Ecp").text
    browser.quit()
    return finish_text

#
# class TestFeedbackProcess(unittest.TestCase):
#     def setUp(self) -> None:
#         self.link = "https://devs.culturalcalculator.co.uk/feedback-process/2ebfb840-886b-4f3b-8123-0ab1bb072364"
#
#     def tearDown(self) -> None:
#         pass

    # def test_feedback_process(self):
    #     self.assertEqual(feedback_process(self.link), "We have now received your feedback.", "Feedback is not passed")

    # def test_multiply(self):
    #     self.assertEqual(2 * 2, 4)
    #
    # def test_plus(self):
    #     self.assertEqual(2 + 2, 4)
    #
    # def test_minus(self):
    #     self.assertEqual(2 - 2, 0)


# if __name__ == "__main__":
#     unittest.main()

# buttons

# 1 style="background-color: rgb(44, 42, 67);"
# 2 style="background-color: rgb(55, 65, 104);"

# 3 style="background-color: rgb(66, 87, 141);"
# 4 style="background-color: rgb(78, 111, 179);"

# 5 style="background-color: rgb(89, 133, 216);"
# 6 style="background-color: rgb(101, 157, 254);"

# 7 style="background-color: rgb(109, 177, 249);"
# 8 style="background-color: rgb(117, 196, 245);"

# 9 style="background-color: rgb(124, 216, 242);"
# 10 style="background-color: rgb(132, 235, 238);"
