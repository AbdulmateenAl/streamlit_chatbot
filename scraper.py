from selenium import webdriver
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver  = webdriver.Chrome(options=chrome_options)
driver.get()