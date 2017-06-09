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
        try:
            self.conn = torndb.Connection(host=mysql['host'], database=mysql['db'], user=mysql[
                'user'], password=mysql['passwd'], connect_timeout=60, charset=mysql['charset'])
            # self.conn.autocommit(True)

        except Exception as e:
            print e

    def select(self, sql):

        return self.conn.get(sql)

    def delete(self, sql):
        return self.conn.delete(sql)

    def close(self)
        self.conn.close()
