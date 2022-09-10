import os
import urllib.request
from flask import Flask
from flask import jsonify
import sqlite3
app = Flask(__name__)



def download_migrations_db():
    url = 'https://github.com/dmeneguin/github-actions-database/blob/master/migrations.db?raw=true'
    file_name, headers = urllib.request.urlretrieve(url)
    return file_name


@app.route('/migrations')
def downloadFile ():
    #path = download_migrations_db()
    conn = sqlite3.connect('migrations.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM view_migrations;
    """)

    response = []
    for row in cursor.fetchall():
        response.append(row)

    conn.close()
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





