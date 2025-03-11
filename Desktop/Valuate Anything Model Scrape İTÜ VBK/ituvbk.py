from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By  
from amazoncaptcha import AmazonCaptcha


#selenium yeni ayarları ve agenti yap
options = webdriver.ChromeOptions()
options.add_argument("ser-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
browser = webdriver.Chrome(options=options)

#amazonu aç ve captchayı aş
browser.get("https://www.amazon.com/")
browser.maximize_window()

image_link = browser.find_element(By.XPATH,"//div[@class = 'a-row a-text-center']//img").get_attribute('src')

captcha = AmazonCaptcha.fromlink(image_link)
solution = captcha.solve(captcha)

input_field = browser.find_element(By.ID,"captchacharacters").send_keys(solution)

button = browser.find_element(By.CLASS_NAME, "a-button-text")

button.click()

#amazon arama kısmını ve butonu al
input_search = browser.find_element(By.ID,'twotabsearchtextbox')
search_button = browser.find_element(By.XPATH,"(//input[@type='submit'])[1]")

#arama kısmına döngü şeklinde dictionary eklenerek gezilebilir şimdilik laptop yazıyorum.
input_search.send_keys("Laptop")
search_button.click()

#buraya birdaha bakıcam ben de pek anlamadım ne yazdığımı 
product_class = "s-image"
for i in range(5,10):
    product_xpath = "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[{}]/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div/img".format(i)
    product = browser.find_element(By.XPATH, product_xpath)
    image_link = product.get_attribute('src')
    print(image_link)


