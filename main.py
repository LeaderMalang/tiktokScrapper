from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import traceback
import time

driver = webdriver.Chrome(
    'F:\projects\tiktokScrapper\chromedriver.exe')

driver.get('https://www.tiktok.com/')
