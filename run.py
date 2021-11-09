#!/usr/bin/env python3

from scraper import scrape
import db

def load_items_list():
    urls = []
    with open('items.txt') as file:
        for line in file:
            url = line.rstrip()
            if (len(url) == 0):
                continue
            urls.append(url)
    return urls

def insert_records_into_db(urls):
    items = []

    for url in urls:
        item = db.build_item_from_url(url)
        items.append(item)
    
    return items


db.init()
urls = load_items_list()
items = insert_records_into_db(urls)

for item in items:
    data = scrape(item.url)
    if data is None:
        continue
    print(data.timestamp, data.name, data.price, data.url)

    db.store_price(item, data)

db.close()