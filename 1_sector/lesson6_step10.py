from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    labels = browser.find_elements_by_tag_name('label')
    inputs = browser.find_elements_by_tag_name('input')

    for i, label in enumerate(labels):
        if label.text[-1] == '*':
            inputs[i].send_keys('Обязалово!')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()












