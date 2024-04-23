import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is node", "italic", url=None)
        node2 = TextNode("This is node2", "bold","https://google.com")
        self.assertNotEqual(node, node2)

class TestTextToHTML(unittest.TestCase):

    def test_bold(self):
        node = TextNode("This is bold text", "bold")
        a = text_node_to_html_node(node)
        self.assertEqual(a.__repr__(),"LeafNode(b, This is bold text, None)") 


if __name__ == "__main__":
    unittest.main()
