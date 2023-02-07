#serach image from instragram
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import click as click
from selenium.webdriver.common.action_chains import ActionChains
import os
import wget #下載網頁上的東西
localtime = time.localtime()


count  = 0
result = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.instagram.com/")

#因為跳出頁面前到了一個等待頁面
#所以要先找出登入標籤後才開始輸入

username = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
# actions = ActionChains(driver)
# actions.move_to_element(driver.find_element(By.CLASS_NAME,"_2hvTZ ")).perform
# actions.perform()
username.clear()
username.send_keys("jentingtyu")
password.clear()
time.sleep(2)
password.send_keys("Mme0608623")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(2)

#關掉是否儲存登入資訊
# check = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))
#     )
# driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click() #這行有跑
#
# #關掉是否開啟通知 /html/body/div[5]/div/div/div/div[3]/button[2]
# noise = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))
#     )
#
# driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]').click()

#進行收尋
#左邊列表放大鏡按鈕
search1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div'))
    )
search1 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div').click()

search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'))
    )
serach = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
keyword = "#cat"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "x5yr21d"))
    )


imgs = driver.find_elements(By.CLASS_NAME,"x5yr21d")


# x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3
path = os.path.join(keyword) #當作資料夾路徑
# os.mkdir(path)#創建資料夾


for img in imgs:
    #save_as = os.path.join(path,keyword + str(count) + 'jpg') #keyword = cat 檔名 cat1 cat2 cat3...
    print('AFAF',img.get_attribute("src"))#下載要取得屬性src
    #wget.download(img.get_attribute('src'), save_as) #傳入圖片的位置,宣告電腦哪個地方
    #count = count + 1
print("ty")
time.sleep(10)
