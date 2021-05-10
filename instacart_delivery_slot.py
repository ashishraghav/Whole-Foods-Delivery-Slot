import bs4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import sys
import time
import os


def getWFSlot(productUrl):
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
   }

   driver = webdriver.Chrome('c:/git/lib/chromedriver')
   #driver = webdriver.Chrome()
   driver.get(productUrl)           
   time.sleep(5)
   driver.find_element_by_id('nextgen-authenticate.all.log_in_email').send_keys('instacart@raghavzone.com')
   driver.find_element_by_id('nextgen-authenticate.all.log_in_password').send_keys('Ashish123')
   #driver.find_element(By.ID, “loginbutton”).click()   

   element = driver.find_element(By.CSS_SELECTOR, ".rmq-db5b060a")
   actions = ActionChains(driver)
   actions.move_to_element(element).perform()
   element = driver.find_element(By.CSS_SELECTOR, "body")
   actions = ActionChains(driver)
   actions.move_to_element(element, 0, 0).perform()
   driver.find_element(By.CSS_SELECTOR, "span > a > span").click()
   driver.find_element(By.ID, "react-tabs-2").click()
   driver.find_element(By.CSS_SELECTOR, ".icModalClose i").click()
   driver.find_element(By.CSS_SELECTOR, "span > a > span").click()
   driver.find_element(By.CSS_SELECTOR, "h1").click()
   driver.find_element(By.ID, "react-tabs-8").click()
   driver.find_element(By.CSS_SELECTOR, ".rmq-32e4a8df img").click()
   driver.find_element(By.CSS_SELECTOR, "h1").click()
   driver.find_element(By.CSS_SELECTOR, ".rmq-32e4a8df > .module-wrapper > div").click()
   
   
   
   html = driver.page_source
   soup = bs4.BeautifulSoup(html)
   time.sleep(15)
   no_open_slots = True


   while no_open_slots:
      driver.refresh()
      print("refreshed")
      html = driver.page_source
      soup = bs4.BeautifulSoup(html)
      time.sleep(10)

      try:
         no_slot_pattern = 'No delivery windows available. New windows are released throughout the day.'
         slot_pattern_extract = soup.find('h4', class_ ='a-alert-heading').text
         print(slot_pattern_extract)
         if no_slot_pattern == slot_pattern_extract:
            print("NO SLOTS!")
      except AttributeError: 
            print('SLOTS OPEN!')
            os.system('say "Slots for delivery opened!"')
            #no_open_slots = False


      slot_pattern = 'Next available'
      try:
         next_slot_text = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal').text
         if slot_pattern in next_slot_text:
            print('SLOTS OPEN!!')
            os.system('say "Slots for delivery opened!!"')
            no_open_slots = False
            time.sleep(1400)
      except AttributeError:
         continue



getWFSlot('https://www.instacart.com/store/acme-markets/storefront')


