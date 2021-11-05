#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from scraper_factory import buid_scraper


url = "https://www.tannico.it/morellino-di-scansano-riserva-docg-purosangue-2017-terenzi.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
}

scraper = buid_scraper(url)
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

price = scraper.ScrapePrice(soup)
name = scraper.ScrapeName(soup)

print(name)
print(price)
