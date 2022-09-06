import sqlite3

conn = sqlite3.connect('migrations.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM migrations;
""")

for row in cursor.fetchall():
    print(row)

conn.close()