import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import wget
import click as click


driver = webdriver.Chrome('./chromedriver')
driver.get("https://ithelp.ithome.com.tw/articles/10300961")
time.sleep(1)

