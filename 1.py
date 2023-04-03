import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    "mobileEmulation",
    {"deviceName": "iPhone 5"})
driver = webdriver.Chrome(executable_path='driver/chromedriver.exe', desired_capabilities=chrome_options.to_capabilities())
driver.maximize_window()
driver.get("https://apitest.mshchina.com/wechat/#/login?openid=o_YpJwjcmoetXsDKJCBb9AEOvkSM&state=02&language=zh_cn")
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/div[2]/div/div/input').send_keys('EBS-0058')
driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/div[4]/div/div/input').send_keys('Msh1234567')
driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/div[1]/div').click()
driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
# time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="home"]/div[1]/div[3]/div[1]/div[1]/div[2]').click()
driver.find_element(By.CSS_SELECTOR, '.button_middle').click()

# driver.switch_to.frame()frame
driver.find_element(By.CSS_SELECTOR, '.van-button').click()
# driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, '.van-button'))

a = False
print(a)
