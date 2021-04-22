from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = 'C:\chromedriver\chromedriver.exe'
USERNAME = '#TODO: CHANGE USERNAME'
PASSWORD = '#TODO: CHANGE PASSWORD'


driver = webdriver.Chrome(CHROME_DRIVER_PATH)


driver.get('https://www.speedtest.net/')
start_button = driver.find_element_by_class_name('start-text')
start_button.click()
time.sleep(60)
download = driver.find_element_by_css_selector(
    'div .download-speed').text
upload = driver.find_element_by_css_selector(
    'div .upload-speed').text
print(f'download speed: {download}')
print(f'upload speed: {upload}')

# Go to twitter
driver.get(
    r'https://twitter.com/login'
)
username = driver.find_element_by_name(
    'session[username_or_email]'
)
password = driver.find_element_by_name(
    'session[password]'
)
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)
tweet = driver.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
)
tweet.send_keys(
    f'Send from my first bot using web scrapping :). Download speed internet: {download} and upload: {upload}'
)
tweet_button = driver.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span'
)
tweet_button.click()
