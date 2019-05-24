# file name : dbModule.py
# pwd : /project_name/app/module/dbModule.py

import pymysql


class Database():
    def __init__(self):
        self.db = pymysql.connect('localhost','root','1234','redbook')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def recentCrawledBook(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        self.db.close()
        return row