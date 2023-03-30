from shared.connection import db

def get_message(id):
    cursor = db.cursor()
    res = cursor.execute('SELECT * FROM messages WHERE id = ?', (id,)).fetchone()
    cursor.close()
    if res is None:
        return {}, 404
    return dict(res), 200
    
def save_message(adict):
    message = adict['message']
    cursor = db.cursor()
    cursor.execute('INSERT INTO messages (message) VALUES (?)', (message,))
    row_id = cursor.lastrowid
    db.commit()
    cursor.close()
    return row_id, 200