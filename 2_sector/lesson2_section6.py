from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    value = browser.find_element_by_xpath("//span[@id='input_value']")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = value.text
    y = calc(x)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 100);", button)  # ("return arguments[0]; scrollIntoView(true);", button)
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    radiobutton = browser.find_element_by_xpath("//input[@id='robotsRule']").click()
    button.click()


finally:
    time.sleep(10)
    browser.quit()














