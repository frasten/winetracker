class MonitoredItem():
    id = 0
    url = ''
    name = ''
    timestamp_added = None
    enabled = True
    
    def __init__(self):
        pass
    
    def __init__(self, db_row):
        self.id = db_row[0]
        self.url = db_row[1]
        self.name = db_row[2]
        self.timestamp_added = db_row[3]
        self.enabled = (db_row[4] == 1)