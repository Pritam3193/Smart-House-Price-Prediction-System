import sqlite3

conn = sqlite3.connect("housing.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    area REAL,
    bedrooms INTEGER,
    bathrooms INTEGER,
    stories INTEGER,
    predicted_price REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")