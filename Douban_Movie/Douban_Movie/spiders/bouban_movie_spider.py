from scrapy import Request
from scrapy.spiders import Spider
from Douban_Movie.items import DoubanMovieItem

class DoubanMovieSpider(Spider):
    name = 'douban_movie_spider'
    # start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    url = 'https://movie.douban.com/top250'
    heards = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }

    def start_requests(self):
        rootURL = self.url + '?start=0&filter='
        # rootURL = 'https://movie.douban.com/top250?start=0&filter='
        yield Request(rootURL, headers=self.heards)

    def parse(self, response):

        print(response)

        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item = DoubanMovieItem()
            item['movieTopNum'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['movieName'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['movieDetailURL'] = movie.xpath('.//div[@class="hd"]/a/@href').extract()[0]
            item['movieImageURL'] = movie.xpath('.//div[@class="pic"]/a/img/@src').extract()[0]
            item['movieRating'] = movie.xpath('.//div[@class="star"]/span[2]/text()').extract()[0]
            item['movieDirector'] = movie.xpath('normalize-space(.//div[@class="bd"]/p/text())').extract()[0]
            item['movieActors'] = ''

            introduce = movie.xpath('.//div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            item['movieIntroduce'] =  introduce[0] if introduce else " "
            yield item

        nextPage_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if nextPage_url:
            nextPage_url = self.url + nextPage_url[0]
            yield Request(nextPage_url, headers=self.heards)