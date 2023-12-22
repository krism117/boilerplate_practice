from selenium.webdriver import ActionChains
import unittest
from browsers.firefox_browser import FirefoxBrowser, FirefoxOptionArguments
from elements.base_web_element import BaseWebElement
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from elements.input import Input
from elements.checkbox import Checkbox
from elements.button import Button
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_case = unittest.TestCase()

s = Service('geckodriver.exe')
driver = webdriver.Firefox(service=s)




# Create instance with default options
driver.get('https://demoqa.com/')

# Open elements page
elements = BaseWebElement(parent= driver, locator=(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
elements.click()

textBox_tab = BaseWebElement(parent=driver, locator=(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]'))
textBox_tab.click()

fullname_text = 'John Smith'
fullname_field = Input(parent=driver, locator=(By.ID, 'userName'))
fullname_field.enter_value(fullname_text, clear_first=False)

email_text = 'js@email.com'
email_field = Input(parent=driver, locator=(By.ID, 'userEmail'))
email_field.enter_value(email_text, clear_first=False)

currentAddress_text = '123 New Street'
currentAddress = Input(parent=driver, locator=(By.ID, 'currentAddress'))
currentAddress.enter_value(currentAddress_text, clear_first=False)

permenantAddress_text = '123 Station Road'
permenantAddress = Input(parent=driver, locator=(By.ID, 'permanentAddress'))
permenantAddress.enter_value(permenantAddress_text, clear_first=False)

#open check box tab
checkbox_tab = BaseWebElement(parent= driver, locator=(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]'))
checkbox_tab.click()

checkbox = Checkbox(parent=driver, locator=(By.CLASS_NAME, 'rct-checkbox'))
checkbox.check()

open_home = BaseWebElement(parent=driver, locator=(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/span[1]/button[1]/*[name()='svg'][1]"))
open_home.click()

downloads_checkbox = Checkbox(parent=driver, locator=(By.XPATH, "//label[@for='tree-node-downloads']//span[@class='rct-checkbox']//*[name()='svg']"))
downloads_checkbox.check()

#open radio Button_tab
radioButton_tab = BaseWebElement(parent= driver, locator=(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/span[1]'))
radioButton_tab.click()

yes_radio = Button(parent=driver, locator=(By.XPATH, "//label[@for='yesRadio']"))
yes_radio.click()

#web tables tab
web_tables_tab = BaseWebElement(parent=driver, locator=(By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-3']"))
web_tables_tab.click()

add_row = BaseWebElement(parent=driver, locator=(By.XPATH, "//button[@id='addNewRecordButton']"))
add_row.click()

update_fname_text = 'John'
update_fname = Input(parent=driver, locator=(By.XPATH, "//input[@id='firstName']"))
update_fname.enter_value(update_fname_text, clear_first=False)

update_lname_text = 'Doe'
update_lname = Input(parent=driver, locator=(By.XPATH, "//input[@id='lastName']"))
update_lname.enter_value(update_lname_text, clear_first=False)

update_email_text = 'jdoe@email.com'
update_email = Input(parent=driver, locator=(By.XPATH, "//input[@id='userEmail']"))
update_email.enter_value(update_email_text, clear_first=False)

update_age_text = '34'
update_age = Input(parent=driver, locator=(By.XPATH, "//input[@id='age']"))
update_age.enter_value(update_age_text, clear_first=False)

update_salary_text = '25000'
update_salary = Input(parent=driver, locator=(By.XPATH, "//input[@id='salary']"))
update_salary.enter_value(update_salary_text, clear_first=False)


update_department_text = 'Goods In'
update_department = Input(parent=driver, locator=(By.XPATH, "/html//input[@id='department']"))
update_department.enter_value(update_department_text, clear_first=False)

submit_button = Input(parent=driver, locator=(By.ID, "submit"))
submit_button.click()

#open buttons tab
web_buttons_tab = BaseWebElement(parent=driver, locator=(By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-4']"))
web_buttons_tab.click()

click_button = Button(parent=driver, locator=(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/button[1]"))
click_button.click()
text_locator = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/p[1]")
wait = WebDriverWait(driver, 10)
text_element = wait.until(EC.visibility_of_element_located(text_locator))

displayed_text = (text_element.text)
expected_text = ("You have done a dynamic click")
print(expected_text)
print(displayed_text)

test_case.assertEqual(displayed_text, expected_text)




#debugging code
time.sleep(5)

# Clean up
driver.quit()