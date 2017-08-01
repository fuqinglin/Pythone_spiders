import requests

class HttpDownloader(object):

    def downloadHtml(self, url):

        rep = requests.get(url)
        rep.encoding = 'utf-8'
        if rep.status_code != 200:
            return
        return rep.text


