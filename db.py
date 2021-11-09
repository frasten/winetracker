import sqlite3
from datetime import datetime

from scraper import ScrapeData, scrape
from monitored_item import MonitoredItem

_db = None

def init():
    global _db
    # Initialize the DB schema:
    with open('db_schema.sql', 'r') as file:
        create_schema_query = file.read()

    _db = sqlite3.connect('winetracker.db')
    cursor = _db.cursor()
    cursor.executescript(create_schema_query)
    _db.commit()
    
def build_item_from_url(url: str) -> MonitoredItem:
    global _db
    cursor = _db.cursor()
    
    cursor.execute('SELECT * FROM item WHERE url=? LIMIT 1', (url,))
    row = cursor.fetchone()
    if row is not None:
        # found
        return MonitoredItem.from_db(row)
    
    scraped = scrape(url)
    if scraped is None:
        raise

    now = datetime.now()
    cursor.execute('INSERT INTO item (url, name, timestamp_added) VALUES (?, ?, ?)', (url, scraped.name, now))
    _db.commit()

    result = MonitoredItem()
    result.name = scraped.name
    result.timestamp_added = now
    result.url = url
    result.id = cursor.lastrowid

    return result

def store_price(item: MonitoredItem, data: ScrapeData):
    global _db

    item_id = item.id
    now = datetime.now()
    price = data.price

    cursor = _db.cursor()
    cursor.execute('INSERT INTO prices (timestamp, item_id, price) VALUES (?, ?, ?)', (now, item_id, price))

    _db.commit()

def close():
    global _db

    _db.close()