from selenium import webdriver
import time
import math

# link1 = "http://suninjuly.github.io/alert_accept.html"
link2 = "http://suninjuly.github.io/alert_redirect.html?"

browser = webdriver.Chrome()
# browser.get(link1)
browser.get(link2)

try:
    # button1 = browser.find_element_by_xpath("//button").click
    # confirm = browser.switch_to.alert.accept()
    value = browser.find_element_by_xpath("//span[@id='input_value']")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = value.text
    y = calc(x)

    button2 = browser.find_element_by_tag_name("button").click
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
finally:
    time.sleep(10)
    browser.quit()






























