import unittest
from inline_markdown import split_nodes_delimeter
from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_code,
        text_type_italic
)

class TestTextInline(unittest.TestCase):
    
    def test_bold_single(self):
        node = TextNode("This is **bold** text", text_type_text)
        new_node = split_nodes_delimeter([node], "**", text_type_bold)
        self.assertListEqual(
                [
                    TextNode("This is ", text_type_text),
                    TextNode("bold", text_type_bold),
                    TextNode(" text", text_type_text)
                ],
                new_node)

    def test_bold_multiple_words(self):
        node = TextNode("This is a test **sentence with** words **bolded**.", text_type_text)
        new_node = split_nodes_delimeter([node], "**", text_type_bold)
        self.assertListEqual(
                [
                    TextNode("This is a test ", text_type_text),
                    TextNode("sentence with", text_type_bold),
                    TextNode(" words ", text_type_text),
                    TextNode("bolded", text_type_bold),
                    TextNode(".", text_type_text)
                ],
                new_node)

    def test_italic(self):
        node = TextNode("This is a test *sentence with* words *italic*.", text_type_text)
        new_node = split_nodes_delimeter([node], "*", text_type_italic)
        self.assertListEqual(
                [
                    TextNode("This is a test ", text_type_text),
                    TextNode("sentence with", text_type_italic),
                    TextNode(" words ", text_type_text),
                    TextNode("italic", text_type_italic),
                    TextNode(".", text_type_text)
                ],
                new_node)

    def test_code(self):
        node = TextNode("This is a test `code block` words `some more code`.", text_type_text)
        new_node = split_nodes_delimeter([node], "`", text_type_code)
        self.assertListEqual(
                [
                    TextNode("This is a test ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" words ", text_type_text),
                    TextNode("some more code", text_type_code),
                    TextNode(".", text_type_text)
                ],
                new_node)
