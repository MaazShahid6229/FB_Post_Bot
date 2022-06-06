# import libraries
import os
import io
import time
import json
import requests
import selenium
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdrivermanager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import commands
from commands import *

# setting chrome extesion
chrome_driver_path = "chromedriver.exe"

# reading Links
f = open("links.txt", "r")
lines = f.readlines()
f.close()

# Handling of Allow Pop Up In Facebook
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})


driver = webdriver.Chrome(chrome_options=option, executable_path=chrome_driver_path)
driver.maximize_window()

# Landing on facebook page
url = "https://web.facebook.com/"
driver.get(url)
time.sleep(2)


# Login
def login(id, password):
    email_element = driver.find_element(By.XPATH, './/*[@id="email"]')
    email_element.send_keys(id)

    pass_element = driver.find_element(By.XPATH, './/*[@id="pass"]')
    pass_element.send_keys(password)

    elem = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
    elem.click()
    time.sleep(3)


# Post Content On FaceBook
def post_content(post):
    driver.get(commands.url)
    time.sleep(3)
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div')
    button.click()
    time.sleep(3)

    post_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div')
    post_element.send_keys(post)

    post_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[3]/div/div/div[1]')
    post_button.click()


login(commands.username, commands.password)
time.sleep(5)

i = 0
for line in lines:
    if i >= 15:
        i = 0
        time.sleep(200)
    print(line)
    try:
        post_content(line)
        time.sleep(10)
    except:
        continue

