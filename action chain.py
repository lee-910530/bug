import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import click as click
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://forum.gamer.com.tw/C.php?bsn=29560&snA=9526")
time.sleep(1)
act = driver.find_element(By.CLASS_NAME,"now")

x = act.get_attribute("data-gtm")
print(x)