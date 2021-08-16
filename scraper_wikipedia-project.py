import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
#import requests as req

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome('chromedriver.exe')
browser.get(START_URL)

time.sleep(10)
headers = ["name", "distance", "mass", "radius", "luminosity"]
stars_data = list()

name_list = list()
distance_list = list()
mass_list = list()
radius_list = list()
luminos_list = list()

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for table in soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"}):
        tbody = table.find("tbody")
        for tr_tags in tbody.find_all("tr"):

            td_tags = tr_tags.find_all("td")

            name_list.append(td_tags[1].text.rstrip())
            distance_list.append(td_tags[3].text.rstrip())
            mass_list.append(td_tags[5].text.rstrip())
            radius_list.append(td_tags[6].text.rstrip())
            luminos_list.append(td_tags[7].text.rstrip())

scrape()

df = pd.DataFrame(list(zip(name_list, distance_list, mass_list, radius_list, luminos_list)), columns = ["name", "distance", "mass", "radius", "luminosity"])

df.to_csv('stars.csv')