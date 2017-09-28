# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    categor = scrapy.Field()
    tag = scrapy.Field()
    tag_url = scrapy.Field()

    pass

class BookInfoItem(scrapy.Item):
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_detailUrl = scrapy.Field()
    book_imgUrl = scrapy.Field()
    book_rating = scrapy.Field()
    book_introduction = scrapy.Field()

    pass
