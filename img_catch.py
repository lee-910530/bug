import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import wget
import click as click

keyword = "LOVE"


driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.google.com/search?q=%E5%90%B3%E9%A6%99%E8%AA%BC&&tbm=isch&ved=2ahUKEwjZ4fDNloH9AhUdQPUHHS4XBjgQ2-cCegQIABAA&oq=%E5%90%B3%E9%A6%99%E8%AA%BC&gs_lcp=CgNpbWcQDDIHCAAQgAQQGDoFCAAQgAQ6CAgAEIAEELEDOgcIIxDqAhAnOgQIIxAnUNEIWNpJYNRpaAFwAHgAgAHPAogB_QaSAQc4LjIuMC4xmAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=FRjhY5mDF52A1e8Prq6YwAM&bih=916&biw=809&rlz=1C1ONGR_zh-TWTW1023TW1023')
# find = driver.find_element(By.XPATH,'//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')
time.sleep(2)
# find.clear()
# find.send_keys(keyword)
# find.send_keys(Keys.ENTER)
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="rso"]/div[2]/div/div/div/div/div/div[1]/div/a/h3')))
#
# driver.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/input').click()
#
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "rg_i")))

for i in range(5) :
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)

#driver.find_element(By.CSS_SELECTOR,'#islmp > div > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input').click()

# for i in range(5) :
#         driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#         time.sleep(2)

imgs = driver.find_elements(By.CLASS_NAME, "rg_i")

path = os.path.join("LOVE")
os.mkdir(path)

count = 0
for img in imgs:
        if  img.get_attribute("src") != None :   #None 優先及比較高
                if img.get_attribute("src")[0:4] == 'http':
                        save_as = os.path.join(path, "LOVE" + str(count)+".jpg")
                        wget.download(img.get_attribute("src"),save_as)
                        count +=1
                        # print(img.get_attribute("src"))
                        print