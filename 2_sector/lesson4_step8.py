from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # button = browser.find_element_by_xpath("//button[@id='book']")
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "book"), "$100"))
    button.click()

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











