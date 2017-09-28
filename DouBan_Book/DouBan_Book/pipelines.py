# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from DouBan_Book.items import DoubanBookItem, BookInfoItem

class DoubanBookPipeline(object):

    def open_spider(self, spider):

        try:
            host = settings['MONGODB_HOST']
            port = settings['MONGODB_PORT']
            db_name = settings['MONGODB_DBNAME']

            self.client = pymongo.MongoClient(host=host, port=port)
            self.db = self.client[db_name]

        except :
            print('mongodb open error!')

    def process_item(self, item, spider):

        if isinstance(item, DoubanBookItem):
            self.doubanBook_Catogors = self.db.DoubanBook_Catogors
            self.doubanBook_Catogors.insert(dict(item))

        elif isinstance(item, BookInfoItem):
            table_name = 'DoubanBook_' + settings['BOOK_TAG']
            self.book_Infos = self.db[table_name]
            self.book_Infos.insert(dict(item))

        return item

    def closs_spier(self, spider):
        self.client.close()

