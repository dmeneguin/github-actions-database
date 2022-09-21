import sqlite3
import sys

print(sys.argv[1:])
valid_inputs = json.loads(sys.argv[1:])
print(valid_inputs[0].get('name'))

conn = sqlite3.connect('migrations.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM migrations;
""")

for row in cursor.fetchall():
    print(row)

conn.close()
