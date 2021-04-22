from selenium import webdriver
import time

CHROME_DRIVER_PATH = 'C:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element_by_class_name('top')
time.sleep(0.2)
first_name.send_keys('NW first_name')
last_name = driver.find_element_by_class_name('middle')
time.sleep(0.2)
last_name.send_keys('NW last_name')
email_name = driver.find_element_by_class_name('bottom')
time.sleep(0.2)
email_name.send_keys('NW@test.co')

button = driver.find_element_by_class_name('btn-block')
time.sleep(2)
button.click()
time.sleep(2)

driver.quit()