import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.google.com/')
time.sleep(0.5)         # 0.5초 기다림

search_box = driver.find_element_by_css_selector('.gLFyf.gsfi')
search_box.send_keys('ChromeDriver')
search_box.send_keys(Keys.ENTER) #Keys.RETURN
time.sleep(1)    

