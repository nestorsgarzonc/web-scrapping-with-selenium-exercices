from selenium import webdriver
import time

CHROME_DRIVER_PATH = 'C:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie = driver.find_element_by_id('bigCookie')
time.sleep(2)
for i in range(100000):
    cheapest_boost = driver.find_elements_by_xpath(
        '//div[@class="product unlocked enabled"]'
    )
    if len(cheapest_boost) > 0:
        cheapest_boost[len(cheapest_boost)-1].click()
    cookie.click()
