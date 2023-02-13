import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import wget
import click as click

keyword = "HI"


driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.google.com/")
time.sleep(1)

find = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
time.sleep(1)
find.clear()
find.send_keys(keyword)
find.send_keys(Keys.ENTER)
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'hdtb-mitem')))

driver.find_element(By.XPATH,'/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]').click()

time.sleep(2)


for i in range(5) :
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)

location = (By.CLASS_NAME,"r0zKGf")

continues = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element(location,"仍要")
)
print(continues)


if continues == True :
        driver.find_element(By.CLASS_NAME,"r0zKGf").click()
        time.sleep(2)
        for i in range(5) :
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(2)

imgs = driver.find_elements(By.CLASS_NAME, "rg_i")
#
path = os.path.join(keyword)
os.mkdir(path)
#
count = 0
for img in imgs:
        if  img.get_attribute("src") != None :   #None 優先及比較高
                if img.get_attribute("src")[0:4] == 'http':
                        save_as = os.path.join(path, keyword + str(count)+".jpg")
                        wget.download(img.get_attribute("src"),save_as)
                        count +=1
