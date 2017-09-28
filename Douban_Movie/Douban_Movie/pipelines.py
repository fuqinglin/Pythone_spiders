# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import sys


class DoubanMoviePipeline(object):

    def __init__(self):
        self.file = open('Douban_MovieTop250.md','w')
        # self.file = open('Douban_MovieRank.md','w')

    def process_item(self, item, spider):
        # self.writeTo_md(item)
        self.insertTo_DB(item)
        return item

    def open_spider(self, spider):
        # 连接mongodb 数据库
        try:
            self.client = pymongo.MongoClient('127.0.0.1',27017)
            self.db = self.client.MovieDB
            self.movies = self.db.movies_top250
        except:
            print('error:',sys.exc_info())

    # 数据写入MarkDown文本
    def writeTo_md(self, item):
        topNum = item['movieTopNum']
        name = item['movieName']
        detailURL = item['movieDetailURL']
        rating = item['movieRating']
        director = item['movieDirector']
        actors = item['movieActors']
        imageURL = item['movieImageURL']
        introduce = item['movieIntroduce']

        self.file.write('\n###{}、[{}]({}) —— {}\n'.format(topNum, name, detailURL, rating))
        # self.file.write('\n*{}*\n'.format(director))
        self.file.write('\n*{}*\n'.format(actors))
        self.file.write('\n![]({})\n'.format(imageURL))
        self.file.write('\n{}'.format(introduce))
        self.file.write('\n***\n')

    # 数据写入数据库
    def insertTo_DB(self, item):

        movie = dict(item)
        self.movies.insert(movie)

    def close_spider(self,spider):
        self.file.close()
        self.client.close()

