import sqlite3
from datetime import date

conn = sqlite3.connect('migrations.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='migrations';")
migrations_exists = cursor.fetchone()

if migrations_exists == None:
    cursor.execute("""
    CREATE TABLE migrations (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
    );
    """)
    print('Tabela migrations criada com sucesso.')
else:
    print('Tabela migrations já existe.')

today = date.today()
insert_query = "INSERT INTO migrations (nome) VALUES ('"+str(today)+"')";
cursor.execute(insert_query)
conn.commit()

conn.close()
a= [
    {'name':'teste1', 'success':true},
    {'name':'teste2', 'success':false},
    {'name':'teste3', 'success':false}
]
print(f"::set-output ::group::Validated Objects")
print(json.dumps(a))
print(f"::endgroup::")
