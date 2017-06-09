# encoding:utf-8
# dbutil.py

from app.conf.config import MySQLConnection as mysql
try:
    import torndb
except Exception as e:
    print e


class DB:
    conn = None
    host = None
    db = None

    def connect(self):
        conn = torndb.Connection(host=mysql.host)
