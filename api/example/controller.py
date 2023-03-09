import sqlite3
import mysql.connector as mysql
from shared.db import db

def get_message(id):
    cursor = db.cursor()
    res = cursor.execute('SELECT * FROM messages WHERE id = ?', (id,)).fetchone()
    cursor.close()
    return dict(res) if not res is None else None

def save_message(adict):
    message = adict['message']
    cursor = db.cursor()
    cursor.execute('INSERT INTO messages (message) VALUES (?)', (message,))
    row_id = cursor.lastrowid
    db.commit()
    cursor.close()
    return row_id