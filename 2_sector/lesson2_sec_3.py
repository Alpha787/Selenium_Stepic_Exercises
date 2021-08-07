from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element_by_xpath("//span[@id='num1']").text
    num2 = browser.find_element_by_xpath("//span[@id='num2']").text
    result = str(int(num1) + int(num2))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)
    button = browser.find_element_by_xpath("//button").click()

finally:
    time.sleep(10)
    browser.quit()







