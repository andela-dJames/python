import unittest
from parser import Parser

class ParserTest(unittest.TestCase):

    def test_passage_is_parsed(self):

        html_doc = '''
        <div class="passage-text">
            <div class="passage-wrap">
                <div class="passage-content passage-class-0">
                    <div class="version-KJV result-text-style-normal text-html">
                        <h1 class="passage-display">
                            <span class="passage-display-bcv">Mark 1:1</span>
                            <span class="passage-display-version">King James Version (KJV)</span>
                        </h1>
                        <p class="chapter-1">
                            <span id="en-KJV-24217" class="text Mark-1-1">
                                <span class="chapternum">1&nbsp;</span>
                                The beginning of the gospel of Jesus Christ, the Son of God;
                            </span>
                        </p>
                    </div>
                    <div class="publisher-info-bottom with-single">
                        <strong>
                            <a href="/versions/King-James-Version-KJV-Bible/">King James Version</a> 
                            (KJV)
                        </strong> 
                        <p>
                            <a href="https://support.biblegateway.com/entries/32920140-How-do-I-get-permission-to-use-content-on-your-website-">Public Domain</a>
                        </p>
                    </div>
                    <div class="passage-other-trans">
                        <a href="/verse/en/Mark 1:1">Mark 1:1 in all English translations</a>
                    </div>
                </div>
            </div>
        </div>
        '''

        parser = Parser(html_doc)
        self.assertEqual('The beginning of the gospel of Jesus Christ, the Son of God;'
        , parser.content )

