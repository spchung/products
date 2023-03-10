# sqlite connection
import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
    except Exception as e:
        print(e)

    return conn

def likeify(s):
    return '%'+s+'%'

class QueryBuilder:
    def __init__(self):
        pass

db = create_connection('db.db')
db.row_factory = sqlite3.Row
db.set_trace_callback(print)