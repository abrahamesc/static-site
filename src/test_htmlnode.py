from htmlnode import HTMLNode

import unittest

class TestHTMLNode(unittest.TestCase):
    node = HTMLNode(tag='a', value='This is a link to google.com',children=None, props='' )
