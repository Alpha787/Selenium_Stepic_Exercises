from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    firstname = browser.find_element_by_xpath("//input[@name='firstname']")
    firstname.send_keys("firstname")
    lastname = browser.find_element_by_xpath("//input[@name='lastname']")
    lastname.send_keys("lastname")
    email = browser.find_element_by_xpath("//input[@name='email']")
    email.send_keys("email")
    element = browser.find_element_by_xpath("//input[@name='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test3.txt')
    element.send_keys(file_path)
    button = browser.find_element_by_xpath("//button").click()
finally:
    time.sleep(10)
    browser.quit()
















