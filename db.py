import sqlite3

# Initialize the DB schema:
with open('db_schema.sql', 'r') as file:
    create_schema_query = file.read()

db = sqlite3.connect('winetracker.db')
cursor = db.cursor()

cursor.executescript(create_schema_query)
db.commit()
db.close()