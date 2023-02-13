import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import wget
import click as click
x =[[],[]]
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.youtube.com/")
time.sleep(2)

driver.find_element(By.ID,"guide-icon").click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='發燒影片']")))


hot = driver.find_element(By.XPATH,"//a[@title='發燒影片']//tp-yt-paper-item[1]").click()
time.sleep(2)

find = driver.find_elements(By.ID,"video-title")
fre = driver.find_elements(By.CLASS_NAME,"inline-metadata-item.style-scope.ytd-video-meta-block")

for i in find:
    x[0].append(i.get_attribute("title"))
for f in fre :
    x[1].append(f.text)
print(list(filter(lambda z: z!="",x[0])))
print(x[1])

# <a id="video-title" class="yt-simple-endpoint style-scope ytd-video-renderer" title="全場低氣壓！壓力山大的一對一環節｜嚴峻的賽制 選手們頻頻失誤 評審陳星翰氣到發抖｜FULL 正片｜EP4 MIC 2 MIC 正面交鋒 (上)｜大嘻哈時代2｜BingX" aria-label="全場低氣壓！壓力山大的一對一環節｜嚴峻的賽制 選手們頻頻失誤 評審陳星翰氣到發抖｜FULL 正片｜EP4 MIC 2 MIC 正面交鋒 (上)｜大嘻哈時代2｜BingX 上傳者：大嘻哈時代 The Rappers 6 天前 1 小時 36 分鐘 觀看次數：443,827次" href="/watch?v=X9IxL63GkVc">
#             <yt-icon id="inline-title-icon" class="style-scope ytd-video-renderer" hidden=""><!--css-build:shady--></yt-icon>
#             <yt-formatted-string class="style-scope ytd-video-renderer" aria-label="全場低氣壓！壓力山大的一對一環節｜嚴峻的賽制 選手們頻頻失誤 評審陳星翰氣到發抖｜FULL 正片｜EP4 MIC 2 MIC 正面交鋒 (上)｜大嘻哈時代2｜BingX 上傳者：大嘻哈時代 The Rappers 6 天前 1 小時 36 分鐘 觀看次數：443,827次">全場低氣壓！壓力山大的一對一環節｜嚴峻的賽制 選手們頻頻失誤 評審陳星翰氣到發抖｜FULL 正片｜EP4 MIC 2 MIC 正面交鋒 (上)｜大嘻哈時代2｜BingX</yt-formatted-string>
#           </a>
#
# <a id="video-title" class="yt-simple-endpoint style-scope ytd-video-renderer" title="#鄧超 跳舞有多絕？穿豹紋服跳魔性廣場舞，直接把孫儷給整崩潰了！" aria-label="#鄧超 跳舞有多絕？穿豹紋服跳魔性廣場舞，直接把孫儷給整崩潰了！ 上傳者：中国影视优视频 6 天前 20 秒 觀看次數：768,945次 - 播放 Shorts" href="/shorts/ZtsE82GSUGM">
#             <yt-icon id="inline-title-icon" class="style-scope ytd-video-renderer" hidden=""><!--css-build:shady--></yt-icon>
#             <yt-formatted-string class="style-scope ytd-video-renderer" aria-label="#鄧超 跳舞有多絕？穿豹紋服跳魔性廣場舞，直接把孫儷給整崩潰了！ 上傳者：中国影视优视频 6 天前 20 秒 觀看次數：768,945次 - 播放 Shorts">#鄧超 跳舞有多絕？穿豹紋服跳魔性廣場舞，直接把孫儷給整崩潰了！</yt-formatted-string>
#           </a>

