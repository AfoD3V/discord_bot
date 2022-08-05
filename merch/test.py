import time
import re

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os

# Instantiate options
opts = Options()

opts.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

# Location of webdriver
s = Service("C:/Users/Danny/OneDrive/Pulpit/chromedriver_win32/chromedriver")

# Instantiate webdriver
driver = webdriver.Chrome(service=s)

website = 'https://lostmerchants.com/'
driver.get(website)

# Waiting time for site content to load
driver.implicitly_wait(10)

# Selecting region from list
region = driver.find_element(By.ID, 'severRegion')
drp_region = Select(region)
drp_region.select_by_visible_text('EU Central')

# Selecting server from list
server = driver.find_element(By.ID, 'server')
drp_region = Select(server)
drp_region.select_by_visible_text('Procyon')

time.sleep(4)

soup = BeautifulSoup(driver.page_source, 'lxml')
tables = soup.find_all('span', {'class': 'item Epic'})  # <span class="item Epic"

for i in tables:
    text = str(i)
    prepared_string = re.split("[<>]", text)
    print(prepared_string[2])

tables_NPC = soup.find_all('tbody')

with open('html.txt', 'w') as f:
    f.write(str(tables_NPC))

for i in tables_NPC:
    print(i)

# dfs = pd.read_html((str(tables)))
# print(dfs)

driver.quit()
