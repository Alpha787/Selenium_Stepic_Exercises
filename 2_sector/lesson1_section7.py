from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    find_treasure = browser.find_element_by_id('treasure')
    find_chest_attr = find_treasure.get_attribute('valuex')

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x = find_chest_attr
    y = calc(x)

    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    robot_check = browser.find_element_by_xpath("//input[@class='check-input'][@type='checkbox']")
    robot_check.click()
    robots_rule = browser.find_element_by_xpath("//input[@class='check-input'][@type='radio'][@value='robots']")
    robots_rule.click()
    button = browser.find_element_by_xpath("//button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
















