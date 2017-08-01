
class HtmlOutPuter(object):

    def wirtTo_macdown(self, fileName, datas):
        topNumber = 1
        file = open('{}.md'.format(fileName), 'w', encoding='utf-8')
        for bookInfo in datas:
            detailURL = 'https://read.douban.com{}'.format(bookInfo['detailURL'])
            authorURL = 'https://read.douban.com{}'.format(bookInfo['authorURL'])
            file.write('##{}、[{}]({}) —— {}\n'.format(topNumber,bookInfo['title'],detailURL ,bookInfo['rating']))
            file.write('\n*作者：[{}]({})*\n'.format(bookInfo['author'], authorURL))
            file.write('\n![]({})\n'.format(bookInfo['imageURL']))
            file.write('\n{}\n'.format(bookInfo['introduction']))
            file.write('***\n')
            topNumber += 1
        file.close()



