from scrapy.spiders import Spider
from scrapy import Request
from scrapy.conf import settings
from DouBan_Book.items import BookInfoItem
import pymongo


class BooksSpider(Spider):
    name = 'Douban_books_spider'
    base_url = 'https://book.douban.com'

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']

        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[db_name]
        self.DoubanBook_Catogors = self.db.DoubanBook_Catogors
        self.start_urls = self.load_urls_from_db({'tag':settings['BOOK_TAG']})
        if  not self.start_urls:
            self.start_urls.append(self.base_url + '/tag/' + settings['BOOK_TAG'])

    def load_urls_from_db(self, condition):

        datas = self.DoubanBook_Catogors.find(condition)
        urls = []
        for data in datas:
            urls.append(data['tag_url'])
        return urls

    def parse(self, response):

        bookInfos = response.xpath('.//div[@id="subject_list"]/ul/li')
        for book in bookInfos:
            try:
                info = book.xpath('./div[@class="info"]')
                name = info.xpath('./h2/a/@title').extract()
                detailUrl = info.xpath('./h2/a/@href').extract()
                author = info.xpath('./div[@class="pub"]/text()').extract()
                rating = info.xpath('./div[@class="star clearfix"]/span[@class="rating_nums"]/text()'). extract()
                introduction = info.xpath('./p/text()').extract()
                img_url = book.xpath('./div[@class="pic"]/a/img/@src').extract()

                item = BookInfoItem()
                item['book_name'] = name[0] if name else ' '
                item['book_author'] = author[0].strip() if author else ' '
                item['book_detailUrl'] = detailUrl[0] if detailUrl else ' '
                item['book_rating'] = rating[0] if rating else '0.0'
                item['book_imgUrl'] = img_url[0] if img_url else ' '
                item['book_introduction'] = introduction[0].strip() if introduction else ' '
                yield item

            except:
                print('error')

        next_url = response.xpath('.//div[@id="subject_list"]/div[@class="paginator"]/span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = self.base_url + next_url[0]
            yield Request(next_url)

    # def start_requests(self):
    #
    #
    #     return