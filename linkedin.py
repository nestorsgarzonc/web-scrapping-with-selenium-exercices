from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

CHROME_DRIVER_PATH = 'C:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get(
    r'https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=python%20developer'
)
login_button = driver.find_element_by_xpath('/html/body/header/nav/div/a[2]')
login_button.click()

time.sleep(3)
email = driver.find_element_by_id('username')
email.click()
email.send_keys('#TODO: WRITE YOUR PASSWORD')
password = driver.find_element_by_id('password')
password.click()
password.send_keys(r'#TODO: WRITE YOUR PASSWORD')
password.send_keys(Keys.ENTER)

time.sleep(10)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()
next_button = driver.find_element_by_css_selector(
    "footer button"
)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()
next_button = driver.find_element_by_css_selector(
    "footer button"
)
next_button.click()
