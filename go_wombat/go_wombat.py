from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://gowombat.team/")

# main header
    header1 = browser.find_element(By.CSS_SELECTOR, value=".container h1")
    header_text = header1.text
    assert "Premier Custom Software And Mobile App Development" == header_text, \
        f"{header_text} is not equal 'Premier Custom Software And Mobile App Development'"

# "Why we are different" block
    different_block = browser.find_element(By.CSS_SELECTOR, value=".Home-module--differentTitle--BSn4k h2")
    different_block_text = different_block.text
    assert "Why we are different" == different_block_text, \
        f"{different_block_text} is not equal 'Why we are different'"

# services block
#     ???

# We think with block
    we_think_block = browser.find_element(By.CSS_SELECTOR, value="#gatsby-focus-wrapper .index-module--c-content--csXKh .Home-module--techstack--zeYC9 h2")
    we_think_block_text = we_think_block.text
    assert "We think with" == we_think_block_text, \
        f"{we_think_block_text} is not equal 'We think with'"

# Your project can be deployed to
#     your_project_block = browser.find_element(By.CSS_SELECTOR, value=".wrapper .Home-module--adviceContainer--mOo93 h2")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", your_project_block)
#     your_project_block_text = your_project_block.text
#     print(your_project_block_text)
#     assert "Your project can be deployed to" == your_project_block_text

# Industries where we excel
    industries_block = browser.find_element(By.CSS_SELECTOR, value=".Home-module--expertise--nm4SI .wrapper>h2")
    browser.execute_script("return arguments[0].scrollIntoView(true);", industries_block)
    industries_block_text = industries_block.text
    assert "Industries where we excel" == industries_block_text, \
        f"{industries_block_text} is not equal 'Industries where we excel'"
    time.sleep(2)
# Do you have a business in another field?
    another_field_block = browser.find_element(By.CSS_SELECTOR, value=".Home-module--anotherBusinessTitle--ljeC0>h2")
    browser.execute_script("return arguments[0].scrollIntoView(true);", another_field_block)
    another_field_block_text = another_field_block.text
    assert "Do you have a business in another field?" == another_field_block_text, \
        f"{another_field_block_text} is not equal 'Do you have a business in another field?'"
    time.sleep(2)
# About company
    about_comp = browser.find_element(By.CSS_SELECTOR, value=".Home-module--aboutTextContainer--yX09O>h2")
    browser.execute_script("return arguments[0].scrollIntoView(true);", about_comp)
    about_comp_text = about_comp.text
    assert "About company" == about_comp_text, \
        f"{about_comp_text} is not equal 'About company'"
    time.sleep(2)
# Test the might of our R&D team
    test_the_might = browser.find_element(By.CSS_SELECTOR, value=".Home-module--rdteamTitle--DvoBX>h2")
    browser.execute_script("return arguments[0].scrollIntoView(true);", test_the_might)
    test_the_might_text = test_the_might.text
    assert "Test the might of our R&D team" == test_the_might_text, \
        f"{test_the_might_text} is not equal 'Test the might of our R&D team'"
    time.sleep(2)
# Our Awards and Recommendations
    our_awards = browser.find_element(By.CSS_SELECTOR, value=".Home-module--awards--YpCY1 .wrapper>h2")
    browser.execute_script("return arguments[0].scrollIntoView(true);", our_awards)
    our_awards_text = our_awards.text
    assert "Our Awards and Recommendations" == our_awards_text, \
        f"{our_awards_text} is not equal 'Our Awards and Recommendations'"
    time.sleep(2)
# We really believe in the value of face to face meetings
    we_believe = browser.find_element(By.CSS_SELECTOR, value=".Home-module--meetUsContent--K5EHK h2")
    browser.execute_script("return arguments[0].scrollIntoView(true);", we_believe)
    we_believe_text = we_believe.text
    assert "We really believe in the value of face to face meetings" == we_believe_text, \
        f"{we_believe_text} is not equal 'We really believe in the value of face to face meetings'"
    time.sleep(2)
# Clients & Testimonials
    clients = browser.find_element(By.CSS_SELECTOR, value=".Home-module--testimonials--oihzh>h2")
    browser.execute_script("return arguments[0].scrollIntoView(true);", clients)
    clients_text = clients.text
    assert "Clients & Testimonials" == clients_text, \
        f"{clients_text} is not equal 'Clients & Testimonials'"
    time.sleep(2)
# FAQ
    faq_block = browser.find_element(By.CSS_SELECTOR, value=".Home-module--home-faq--5Ee8P .container h2")
    browser.execute_script("return arguments[0].scrollIntoView(true);", faq_block)
    faq_block_text = faq_block.text
    print(faq_block_text)
    assert "FAQ" == faq_block_text, \
        f"{faq_block_text} is not equal 'FAQ'"
    time.sleep(2)
# FAQ buttons
    faq_button = browser.find_elements(By.CSS_SELECTOR, value=".index-module--accordionButton--5jeaC .index-module--faqAccordionBtn--YT4NQ ")
    for element in faq_button:
        element.click()
        time.sleep(1)

# Stand with Ukraine
    stand_ukr_button = browser.find_element(By.CSS_SELECTOR, value="button.index-module--btnUkraine--wpMJL")
    stand_ukr_button.click()
    stand_ukr_header = browser.find_element(By.CSS_SELECTOR, value=".index-module--modalItem_overflow--sXelK h1")
    stand_ukr_header_text = stand_ukr_header.text
    assert "We Stand With Ukraine" == stand_ukr_header_text, \
        f"{stand_ukr_header_text} is not equal 'We Stand With Ukraine'"
    time.sleep(3)
    stand_ukr_close_button = browser.find_element(By.CSS_SELECTOR, value="button.index-module--modalItem__btn--DCAMA")
    stand_ukr_close_button.click()

# except Exception as E:
#     print(E)
finally:
    time.sleep(3)
    browser.quit()

