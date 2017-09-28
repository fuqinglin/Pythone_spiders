from scrapy import cmdline

# spider_name = 'BookCategory_Spider'
spider_name = 'Douban_books_spider'
cmd = 'scrapy crawl {0}'.format(spider_name)
cmdline.execute(cmd.split())