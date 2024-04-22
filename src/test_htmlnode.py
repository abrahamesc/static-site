import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_parent_no_tag(self):
        node = ParentNode(None, "hello")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_no_value(self):
        node = ParentNode('p', None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_simple_children(self):
        node = ParentNode(
                'div',
                [
                    LeafNode('p', "This is some paragraph."),
                    LeafNode('b', "This is bold text"),
                    LeafNode('i', "This is italics")
                ]
                )
        self.assertEqual(node.to_html(),"<div><p>This is some paragraph.</p><b>This is bold text</b><i>This is italics</i></div>")


    def test_parent_nested_parent(self):
        node = ParentNode(
                'div',
                [
                    LeafNode('p', "This is some paragraph."),
                    LeafNode('b', "This is bold text"),
                    LeafNode('i', "This is italics"),
                    ParentNode(
                        'div',
                        [
                            LeafNode('p', "This is the second paragraph inside the nested Parent"),
                            LeafNode('b', "This is the second bold statement inside the nested Parent")
                        ]
                        )
                ]
                )
        self.assertEqual(
                node.to_html(),
                "<div><p>This is some paragraph.</p><b>This is bold text</b><i>This is italics</i><div><p>This is the second paragraph inside the nested Parent</p><b>This is the second bold statement inside the nested Parent</b></div></div>")

    def test_parent_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
