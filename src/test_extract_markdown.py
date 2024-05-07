import unittest
from inline_markdown import extract_markdown_links, extract_markdown_images

class TestExtractMarkdown(unittest.TestCase):

    def test_links_https(self):
        link = extract_markdown_links("This is some link to [google](https://google.com)")
        self.assertListEqual(link, [("google", "https://google.com")])

    def test_multiple_links(self):
        link = extract_markdown_links("This is some link to [google](https://google.com), and this is a link to [youtube](http://www.youtube.com/ldksjfls)]")
        self.assertListEqual(link, [("google", "https://google.com"), ("youtube", "http://www.youtube.com/ldksjfls")])

    def test_images(self):
        image = extract_markdown_images("This is a ![cat](https://some.website.com/cat.png) image")
        self.assertListEqual(image, [("cat", "https://some.website.com/cat.png")])

    def test_multiple_images(self):
        image = extract_markdown_images("This is a ![cat](https://some.website.com/cat.png) image and a ![dog](https://dog.website.com/dog.png)")
        self.assertListEqual(image, [("cat", "https://some.website.com/cat.png"), ("dog", "https://dog.website.com/dog.png")])
