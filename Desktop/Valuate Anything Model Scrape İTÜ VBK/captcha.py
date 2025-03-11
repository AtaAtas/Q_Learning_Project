from amazoncaptcha import AmazonCaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome() # This is a simplified example

driver.get('https://www.amazon.com/errors/validateCaptcha')

image_link = driver.find_element(By.XPATH,"//div[@class = 'a-row a-text-center']//img").get_attribute('src')

captcha = AmazonCaptcha.fromlink(image_link)
solution = captcha.solve(captcha)

input_field = driver.find_element(By.ID,"captchacharacters").send_keys(solution)

button = driver.find_element(By.CLASS_NAME, "a-button-text")

button.click()
sleep(2500)