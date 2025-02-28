from selenium import webdriver
from selenium.webdriver.common.by import By

firstname = 'Test'
lastname = 'Test2'
email = 'test88@gmail.com'
password = 'Password@1'
confirm_password = 'Password@1'

browser = webdriver.Firefox()
browser.get('https://magento.softwaretestingboard.com/')

#navigatre to Create an Account page
browser.find_element(By.XPATH,'//a[text()="Create an Account"]').click()
browser.find_element(By.ID, 'firstname').send_keys(firstname)
browser.find_element(By.ID, 'lastname').send_keys(lastname)
browser.find_element(By.ID, 'email_address').send_keys(email)
browser.find_element(By.ID, 'password').send_keys(password)
browser.find_element(By.ID, 'password-confirmation').send_keys(confirm_password)
browser.find_element(By.XPATH,'//span[text()="Create an Account"]').click()
