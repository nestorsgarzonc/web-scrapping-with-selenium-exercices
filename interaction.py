from selenium import webdriver
from selenium.webdriver.common.keys import Keys
CHROME_DRIVER_PATH = 'C:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

# statistics = driver.find_element_by_css_selector('#articlecount a')
# print(statistics.text)
# statistics.click()
# # driver.quit()

# all_portals = driver.find_element_by_link_text('All portals')
# all_portals.click()
# driver.wait(10)
input_box = driver.find_element_by_id('searchInput')
# input_box.click()
input_box.send_keys('Flutter')
input_box.send_keys(Keys.ENTER)
driver.wait(10)
element=driver.find_elements_by_class_name('mw-search-result')
element[1].click()