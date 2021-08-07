import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)


try:

    x_element = browser.find_element_by_xpath("//span[@class='nowrap'][@id='input_value']")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_xpath("//input[@id='answer'][@class='form-control']")
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    robots = browser.find_element_by_css_selector("[value='robots']")
    robots.click()
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()





