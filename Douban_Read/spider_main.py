import html_downloader, html_spider, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HttpDownloader()
        self.spider = html_spider.HttpSpider()
        self.outputer = html_outputer.HtmlOutPuter()
        self.allBooks = []

    def startSpider(self, url):
        html_content = self.downloader.downloadHtml(url)
        datas = self.spider.parse_data(html_content)

        for item in datas:
            self.allBooks.append(item)
            print(item)

    def writToFile(self,fileName):
        self.outputer.wirtTo_macdown(fileName,self.allBooks)
        self.allBooks.clear()


if __name__ == '__main__':
# 小说：https://read.douban.com/ebooks/tag/%E5%B0%8F%E8%AF%B4/?cat=book&sort=top&start=0
# 科幻：https://read.douban.com/ebooks/tag/%E7%A7%91%E5%B9%BB/?cat=book&sort=top&start=0
# 历史：https://read.douban.com/ebooks/tag/%E5%8E%86%E5%8F%B2/?cat=book&sort=top&start=0
# 管理：https://read.douban.com/ebooks/tag/%E7%AE%A1%E7%90%86/?cat=book&sort=top&start=0
# 计算机：https://read.douban.com/ebooks/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA/?cat=book&sort=top&start=0
# 心理学：https://read.douban.com/ebooks/tag/%E5%BF%83%E7%90%86%E5%AD%A6/?cat=book&sort=top&start=0

    categorys = {'小说':'https://read.douban.com/ebooks/tag/%E5%B0%8F%E8%AF%B4/?cat=book&sort=top&start=',
                 '科幻':'https://read.douban.com/ebooks/tag/%E7%A7%91%E5%B9%BB/?cat=book&sort=top&start=',
                 '历史':'https://read.douban.com/ebooks/tag/%E5%8E%86%E5%8F%B2/?cat=book&sort=top&start=',
                 '管理':'https://read.douban.com/ebooks/tag/%E7%AE%A1%E7%90%86/?cat=book&sort=top&start=',
                 '计算机': 'https://read.douban.com/ebooks/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA/?cat=book&sort=top&start=',
                 '心理学': 'https://read.douban.com/ebooks/tag/%E5%BF%83%E7%90%86%E5%AD%A6/?cat=book&sort=top&start='
                 }

    spider = SpiderMain()
    for key,value in categorys.items():
        for i in range(0,5):
            baseURL = '{}{}'.format(value,i * 20)
            spider.startSpider(baseURL)

        spider.writToFile('豆瓣读书_{}'.format(key))












