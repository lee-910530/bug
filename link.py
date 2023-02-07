import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import click as click

driver = webdriver.Chrome('./chromedriver')
driver.get('https://forum.gamer.com.tw/B.php?bsn=29560&subbsn=1')

# # x = driver.find_element(By.ID,"gsc-i-id1")
# #                        |  same
x = driver.find_element(By.XPATH,"//*[@id=\"gsc-i-id1\"]")
x.clear()
x.send_keys('堯')
x.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gs-title")))

y = driver.find_elements(By.CLASS_NAME,"gs-title")
for y1 in y :
    print(y1.text)

#link = driver.find_element(By.LINK_TEXT,"【情報】堯 螻蟻之輩... @Sdorica 萬象物語哈啦板- 巴哈姆特").click()

time.sleep(50)



