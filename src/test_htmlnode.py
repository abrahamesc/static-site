from logging import warn
from htmlnode import HTMLNode, LeafNode

import unittest

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode('a',
                        'This is a link to google.com',
                        None,
                        props= {"href": "https://www.google.com","target": "_blank"}
        )                                
        
        self.assertEqual(
                node.props_to_html(),
                ' href="https://www.google.com" target="_blank"'
                )

    def test_to_html_with_props(self):
        node = LeafNode('a',
                        'This is a link to google.com',
                        {"href": "https://www.google.com","target": "_blank"}
        )                                
        
        self.assertEqual(
                node.to_html(),
                '<a href="https://www.google.com" target="_blank">This is a link to google.com</a>'
                )
    
    def test_to_html_no_children(self):
        node = LeafNode('p', "Hello world!")
        self.assertEqual(node.to_html(), '<p>Hello world!</p>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello world!")
        self.assertEqual(node.to_html(), "Hello world!")


if __name__ == "__main__":
    unittest.main()
