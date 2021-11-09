import sqlite3

_db = None

def init():
    # Initialize the DB schema:
    with open('db_schema.sql', 'r') as file:
        create_schema_query = file.read()

    _db = sqlite3.connect('winetracker.db')
    cursor = _db.cursor()
    cursor.executescript(create_schema_query)
    _db.commit()
    _db.close()
    
    
    parameters = (data.timestamp, data.name, data.price)
    cursor.execute('INSERT INTO prices (timestamp, item_id, price) VALUES (?, ?, ?)', ())

def build_item_from_url(url: string) -> MonitoredItem:
    cursor = _db.cursor()
    
    cursor.execute('SELECT * FROM item WHERE url=? LIMIT 1', url)
    row = cursor.fetchone()
    if row is not None:
        # found
        return MonitoredItem(row)
    
    cursor.execute('INSERT INTO item (url, name, timestamp_added) VALUES (?, ?, ?)', (url, name))

def close():
    _db.close()