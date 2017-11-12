from xvfbwrapper import Xvfb
from selenium import webdriver

with Xvfb() as xvfb:
    browser = webdriver.Firefox()
    browser.get('http://www.google.com')
    print(browser.title)
    browser.quit()

