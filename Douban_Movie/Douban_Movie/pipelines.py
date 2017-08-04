# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanMoviePipeline(object):

    def __init__(self):
        # self.file = open('Douban_MovieTop250.md','w')
        self.file = open('Douban_MovieRank.md','w')

    def process_item(self, item, spider):
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

        return item

    def close_spider(self,spider):
        self.file.close()

