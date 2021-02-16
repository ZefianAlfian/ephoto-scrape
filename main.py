from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("/app/.apt/usr/bin/google-chrome")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("/app/.chromedriver/bin/chromedriver"), chrome_options=chrome_options)

driver.get("https://en.ephoto360.com/write-text-on-wet-glass-online-589.html")
time.sleep(4)
text = driver.find_element_by_xpath('/html/body/div[1]/div/section/div/div[1]/form/ul/li[1]/div/div/input')
text.send_keys('zefian')
driver.find_element_by_xpath('/html/body/div[1]/div/section/div/div[1]/form/ul/li[2]/input').click()
time.sleep(5)
driver.close()