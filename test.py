from selenium.webdriver import ActionChains

from browsers.firefox_browser import FirefoxBrowser, FirefoxOptionArguments
from elements.base_web_element import BaseWebElement
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from elements.input import Input
from elements.checkbox import Checkbox
from elements.button import Button
import time

s = Service('geckodriver.exe')
driver = webdriver.Firefox(service=s)

actions = ActionChains(driver)
actions.double_click()


# Create instance with default options
driver.get('https://demoqa.com/')

# Open elements page
elements = BaseWebElement(parent= driver, locator=(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
elements.click()

web_buttons_tab = BaseWebElement(parent=driver, locator=(By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-4']"))
web_buttons_tab.click()

click_button = Button(parent=driver, locator=(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/button[1]"))
click_button.click()
