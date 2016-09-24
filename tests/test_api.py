import unittest

from api import Api

class ApiTest(unittest.TestCase):
    def test_can_fetch_book_chapter_verse(self):
       scripture = Api.fetch('Mark', '1', '1')
       self.assertIn('Mark 1:1', scripture)
