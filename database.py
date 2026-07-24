import sqlite3

DB = "traders.db"

def create_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS traders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        company TEXT,
        country TEXT,
        product TEXT,
        phone TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_trader(data):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO traders
    (name, company, country, product, phone, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()
