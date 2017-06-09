# encoding:utf-8
# dbselect.py
from app.dbutil import DB as db

sql = "select * from t;"
for row in db.select(sql):
    print row
