#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

from utilities import parseItaPrice


URL = "https://www.tannico.it/morellino-di-scansano-riserva-docg-purosangue-2017-terenzi.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("span", class_="new-price")
priceText = results.text
price = parseItaPrice(priceText)

titleTag = soup.find("h1", class_="productPage__title")
print(titleTag.text)

print(price)
