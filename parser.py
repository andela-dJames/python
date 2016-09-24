from bs4 import BeautifulSoup

class Parser(object):
 
    def __init__(self, response):
        self.soup = BeautifulSoup(response, 'html.parser')

    @property
    def content(self):
        passage = self.soup.find('div', class_='passage-content')
        passage_text = passage.find('span', class_='text').text
        return passage_text[passage_text.find('</span>') + 7:].strip()
    

