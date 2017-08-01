from bs4 import BeautifulSoup

class HttpSpider(object):

    def parse_data(self, html_content):

        soup = BeautifulSoup(html_content,'html.parser', from_encoding='utf-8')
        datas = []
        bookList = soup.find('ul',class_='list-lined ebook-list column-list').find_all('li')

        for item in bookList:
            bookInfos = {}
            title = item.find('div',class_='title')
            bookInfos['title'] = title.a.get_text()
            bookInfos['detailURL'] = title.a['href']

            author = item.find('a',class_='author-item')
            bookInfos['author'] = author.get_text()
            bookInfos['authorURL'] = author['href']

            ratingNode = item.find('span',class_='rating-average')
            if  ratingNode == None:
                bookInfos['rating'] = '0.0'
            else:
                bookInfos['rating'] = ratingNode.get_text()

            bookInfos['imageURL'] = item.find('img').get('src')
            bookInfos['introduction'] = item.find('div',class_='article-desc-brief').get_text()
            datas.append(bookInfos)
        else:
            print('没有数据')

        return datas





