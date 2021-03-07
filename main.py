from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import traceback
import time

driver = webdriver.Chrome(
    '/Users/casper.local/Desktop/Dev/job_listing/chromedriver')

driver.get('https://www.crypto-careers.com/jobs/search?d=&l=&lat=&long=&q=crypto')
