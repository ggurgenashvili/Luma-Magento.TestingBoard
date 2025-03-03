from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from SignIn.login import login

browser = webdriver.Firefox()

login(browser, email='guli@gmail.com', password='Password@1')

#add product in cart
def AddToCart():
    browser.find_element(By.XPATH, '//span[text()="Women"]').click()
    browser.find_element(By.XPATH, '(//div[@class="product-item-info"])[1]').click()

    wait = WebDriverWait(browser, 10)
    productSize = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '(//div[@class="swatch-option text"])[1]')))
    productSize.click()
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//div[contains(@class, "swatch-option text selected")]')))

    browser.find_element(By.XPATH, '(//div[@class="swatch-option color"])[1]').click()
    browser.find_element(By.ID, 'product-addtocart-button').click()

AddToCart()