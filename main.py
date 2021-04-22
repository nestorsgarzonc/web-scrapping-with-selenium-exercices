from selenium import webdriver

CHROME_DRIVER_PATH = 'C:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get('https://www.python.org/')
data = driver.find_element_by_xpath(
    '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
)

# Other solution using css selectors
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")

formatted = data    .text.strip().split('\n')
res = {}
counter = 0
for i in range(0, len(formatted), 2):
    res[counter] = {'date': formatted[i], 'event': formatted[i+1]}
    counter += 1
print('#### DATES ####')
print('####  #### ####')
print(res)
print('####  #### ####')
driver.quit()
