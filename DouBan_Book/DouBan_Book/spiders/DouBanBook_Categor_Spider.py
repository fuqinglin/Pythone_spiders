from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
from DouBan_Book.items import DoubanBookItem

class BookCategorySpider(Spider):

    name = 'BookCategory_Spider'
    url = 'https://book.douban.com/tag/'

    def start_requests(self):
        yield Request(self.url, callback=self.parse_items)

    def parse_items(self, response):

        divs = response.xpath('.//div[@class="article"]/div[2]/div')
        for div in divs:
            categor = div.xpath('./a/@name').extract()
            selectors = div.xpath('.//table/tbody/tr')
            self.addItems(categor, selectors)

    def addItems(self, categor, selectors):
        for tr in selectors:
            tds = tr.xpath('.//td')
            for td in tds:
                item = DoubanBookItem()
                tag = td.xpath('./a/text()').extract()[0]
                item['categor'] = categor
                item['tag'] = tag
                item['tag_url'] = self.url + tag
                yield item









