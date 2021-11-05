#!/usr/bin/env python3

from scraper import scrape

urls = [
    'https://www.tannico.it/morellino-di-scansano-riserva-docg-purosangue-2017-terenzi.html',
    'https://www.tannico.it/chablis-aoc-vieilles-vignes-2018-domaine-raoul-gautherin-fils.html',
    ]

for url in urls:
    data = scrape(url)
    print(data.timestamp, data.name, data.price, data.url)