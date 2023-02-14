import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

x =[[],[]]
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.youtube.com/")
time.sleep(2)

driver.find_element(By.ID,"guide-icon").click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='發燒影片']")))


hot = driver.find_element(By.XPATH,"//a[@title='發燒影片']//tp-yt-paper-item[1]").click()
time.sleep(3)

find = driver.find_elements(By.ID,"video-title")
fre = driver.find_elements(By.CLASS_NAME,"inline-metadata-item.style-scope.ytd-video-meta-block")

for i in find:
    x[0].append(i.get_attribute("title"))
for f in fre :
    x[1].append(f.text)
temp = list(filter(lambda z: z != "", x[1]))

title = list(filter(lambda z: z!="",x[0]))
watch = temp[0::2]
z = temp[1::2]

for i,x in zip(title,watch):
    print(i + x +'\n')

