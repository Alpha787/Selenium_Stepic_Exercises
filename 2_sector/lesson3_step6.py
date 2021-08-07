from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element_by_xpath("//button")
    time.sleep(1)
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_xpath("//span[@class='nowrap'][@id='input_value']")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_xpath("//input[@id='answer'][@class='form-control']")
    answer.send_keys(y)

finally:
    time.sleep(10)
    browser.quit()

















