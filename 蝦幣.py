from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('./chromedriver')
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 尝试传参
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2Fshopee-coins')
time.sleep(3)

account = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "loginKey"))
    )
account.clear()
account.send_keys('0970711835')

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
password.clear()
password.send_keys('Lee910530!')
time.sleep(1)
driver.find_elements(By.CSS_SELECTOR,'button')[2].text
'登入'
driver.find_elements(By.CSS_SELECTOR,'button')[2].click()
time.sleep(2)
money = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/main/section[1]/div[1]/div/section"))
    )

driver.find_element(By.CLASS_NAME,'pcmall-dailycheckin_3uUmyu').click()


time.sleep(10)