# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    movieTopNum = scrapy.Field()
    movieName = scrapy.Field()
    movieDetailURL = scrapy.Field()
    movieImageURL = scrapy.Field()
    movieRating = scrapy.Field()
    movieDirector = scrapy.Field()
    movieActors = scrapy.Field()
    movieIntroduce = scrapy.Field()

    pass


