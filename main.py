from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import traceback
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(
    'F:\\projects\\tiktokScrapper\\chromedriver.exe', options=options)


driver.get('https://www.tiktok.com/')
action = ActionChains(driver)
infulencers = driver.find_elements(By.CSS_SELECTOR, '.author-uniqueId')
for infulencer in infulencers:
    action.move_to_element(infulencer).perform()
    print(infulencer.text)
