import requests

API_URL = 'https://www.biblegateway.com/passage/'

class Api(object):

    @staticmethod
    def fetch(book, chapter, verse):
        payload = {
            'search': '{} {}:{}'.format(book, chapter, verse), 
            'version': 'KJV'
        }
        response = requests.get(API_URL, params=payload)
        return str(response.content)
