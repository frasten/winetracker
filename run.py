#!/usr/bin/env python3

from scraper import scrape

urls = [
    'https://www.tannico.it/morellino-di-scansano-riserva-docg-purosangue-2017-terenzi.html',
    'https://www.tannico.it/chablis-aoc-vieilles-vignes-2018-domaine-raoul-gautherin-fils.html',
    'https://www.vino.com/dettaglio/valpolicella-ripasso-superiore-doc-collezione-del-conte-villa-da-filicaja-2017.html',
    'https://www.vino.com/dettaglio/franciacorta-rose-nature-docg-61-berlucchi-2014.html',
    'https://www.vino.com/dettaglio/franciacorta-docg-saten-corte-alle-stelle.html',
    'https://www.vinicum.com/i-vini/bundle-valdobbiadene-prosecco-86055-06.html',
    'https://www.vinicum.com/i-vini/aiace-salice-salentino-riserva-doc-67374-06.html',
    ]

for url in urls:
    data = scrape(url)
    print(data.timestamp, data.name, data.price, data.url)