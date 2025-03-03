from selenium import webdriver
from SignIn.login import login

browser = webdriver.Firefox()

login(browser, email='guli@gmail.com', password='Password@1')

#add product in cart
