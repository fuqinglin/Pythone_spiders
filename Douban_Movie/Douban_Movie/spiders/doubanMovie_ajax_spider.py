from scrapy import Request
from scrapy.spiders import Spider
from Douban_Movie.items import DoubanMovieItem
import json
import re

class DoubanMovieAjaxSpider(Spider):

    name = 'douban_ajax_spider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        datas = json.loads(response.body)
        if datas:
            for data in datas:
                movie = DoubanMovieItem()

                movie['movieTopNum'] = data['rank']
                movie['movieName'] = data['title']
                movie['movieDetailURL'] =data['url']
                movie['movieImageURL'] = data['cover_url']
                movie['movieRating'] = data['score']
                movie['movieActors'] = '演员名单：\n\n{}'.format('、'.join(data['actors']))
                movie['movieIntroduce'] = ''
                movie['movieDirector'] = ''
                yield movie
            start_num = re.search(r'start=(\d+)',response.url).group(1)
            nextPage_num = 'start=' + str(int(start_num) + 20)
            nextPage_url = re.sub(r'start=(\d+)',nextPage_num, response.url)
            yield Request(nextPage_url, headers=self.headers)








