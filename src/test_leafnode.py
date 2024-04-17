
from htmlnode import HTMLNode, LeafNode

import unittest

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = LeafNode('a',
                        'This is a link to google.com',
                        {"href": "https://www.google.com","target": "_blank"}
        )                                
        
        self.assertEqual(
                node.to_html(),
                '<a href="https://www.google.com" target="_blank">This is a link to google.com</a>'
                )
    
if __name__ == "__main__":
    unittest.main()
