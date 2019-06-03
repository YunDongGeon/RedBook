# file name : dbModule.py
# pwd : /project_name/app/module/dbModule.py

import pymongo
import json
from bson import json_util
from jinja2 import UndefinedError

class Database():

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn.get_database("RedBook")             # db선택
        self.collection = self.db.get_collection("booklist")    # 테이블 선택

    def dbclose(self):
        self.conn.close()

    def insert(self, query):
        self.collection.insert(query)

    def execute(self, query):
        self.cursor.execute(query)

    def executeOne(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        return row

    def recentCrawledBook(self):
        rows = self.collection.find().sort('crawled_time', pymongo.DESCENDING).limit(6)
        results = list(rows)
        self.dbclose()
        return json.dumps(results, default=json_util.default, ensure_ascii=False)


    def find(self, keyword):
        print(keyword)
        print("---------------------------------------")
        print(self.collection.find({"title" : keyword }))
        print("---------------------------------------")
        # rows = list(self.collection.find({"title": keyword}).aggregate)

        rows = list(
            self.collection.aggregate([
                {'$sort':{"site":pymongo.DESCENDING, "crawled_time":pymongo.DESCENDING, "price":pymongo.ASCENDING}},
                {'$match': {'title': keyword}},
                {'$group':
                            {
                                '_id': {'isbn':'$isbn', 'site':'$site'},
                                'books': {
                                    '$push':
                                    {
                                        'title': '$title',
                                        'category' : '$category',
                                        'price' : '$price',
                                        'author' : '$author',
                                        'publish' : '$publish',
                                        'publish_date' : '$publish_date',
                                        'img' : '$img',
                                        'url' : '$url',
                                        'crawled_time' : '$crawled_time'
                                    }
                                }
                            }
                        },
                        {'$group':
                            {
                                '_id': {'isbn': '$_id.isbn'},
                                'bookList': { '$push' : {'site' : '$_id.site', 'books' : '$books'}}
                            }
                        }
                    ])
                )
        print('rows 실행')
        results = list(rows)
        self.dbclose()
        return json.dumps(results, default=json_util.default, ensure_ascii=False)
