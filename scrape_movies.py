from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.imdb.com/list/ls566941243/"

def create_table(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(5) # seconds
        new_height = driver.execute_script("return document.body.scrollHeight")

        if height == new_height:
            break
        height = new_height
        time.sleep(5)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    # with open("file.txt", "w", encoding="utf-8") as file:
    #     file.write(str(soup))

    # print("Page content has been saved in file.txt")


    movie_titles = []
    for movie in soup.find_all("li", class_="ipc-metadata-list-summary-item"):
        title = movie.find('h3').text
        spans = movie.find_all('span', class_="sc-b189961a-8 hCbzGp dli-title-metadata-item")
        run_time = None
        # for span in spans:
        #     if 'h' in span:
        #         run_time = span
        #         break

        rating = movie.find('span', class_="ipc-rating-star--rating").text
        movie_titles.append([title, spans, rating])

    driver.quit()

    return movie_titles
print(create_table(url))