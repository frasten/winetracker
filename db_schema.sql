CREATE TABLE IF NOT EXISTS item (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    url             TEXT    NOT NULL,
    name            TEXT,
    timestamp_added DATETIME,
    enabled         INTEGER       DEFAULT (1) 
);

CREATE TABLE IF NOT EXISTS prices (
    id         INTEGER  PRIMARY KEY AUTOINCREMENT,
    timestamp  DATETIME NOT NULL,
    item_id    INTEGER  REFERENCES item (id) NOT NULL,
    price      REAL     NOT NULL
);

CREATE TABLE IF NOT EXISTS notification_setting (
    id         INTEGER      PRIMARY KEY AUTOINCREMENT,
    item_id    INTEGER      REFERENCES item (id),
    threshold  REAL,
    address    TEXT NOT NULL
);
