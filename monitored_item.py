class MonitoredItem():
    id = 0
    url = ''
    name = ''
    timestamp_added = None
    enabled = True
    
    def __init__(self):
        pass
    
    @classmethod
    def from_db(cls, db_row):
        item = cls()
        item.id = db_row[0]
        item.url = db_row[1]
        item.name = db_row[2]
        item.timestamp_added = db_row[3]
        item.enabled = (db_row[4] == 1)

        return item