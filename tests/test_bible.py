import unittest
from bible import Bible

class BibleTest(unittest.TestCase):
    def test_can_open_bible(self):
        text = Bible.open("gennesis", 1, 2)
        self.assertIsNotNone(text)
