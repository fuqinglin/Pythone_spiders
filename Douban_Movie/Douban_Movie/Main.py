from scrapy import cmdline

# spiderName = 'douban_movie_spider'
spiderName = 'douban_ajax_spider'
cmd = 'scarpy crawl {0}'.format(spiderName)
cmdline.execute(cmd.split())