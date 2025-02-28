from selenium import webdriver
from selenium.webdriver.common.by import By


email = 'guli@gmail.com'
password = 'Password@1'

browser = webdriver.Firefox()
browser.get('https://magento.softwaretestingboard.com/')

#navigate to log in page
browser.find_element(By.CLASS_NAME, 'authorization-link').click()
browser.find_element(By.ID, 'email').send_keys(email)
browser.find_element(By.ID, 'pass').send_keys(password)
browser.find_element(By.ID, 'send2').click()

assert browser.find_element(By.CLASS_NAME, 'page-title').is_displayed()