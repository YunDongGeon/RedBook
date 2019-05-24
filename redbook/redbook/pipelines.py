# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors

class RedbookPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', '1234', 'redbook')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # create record if doesn't exist.
        self.cursor.execute(
            "insert into book_list(book_site, book_isbn, book_cat, book_title, book_price, book_author, book_publish, book_publish_date, book_img, book_url, crawl_time) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (item['book_site'],
             item['book_isbn'],
             item['book_cat'],
             item['book_title'],
             item['book_price'],
             item['book_author'],
             item['book_publish'],
             item['book_publish_date'],
             item['book_img'],
             item['book_url'],
             item['crawl_time']))
        self.conn.commit()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
