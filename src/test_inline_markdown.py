import unittest
from inline_markdown import (
        split_nodes_delimeter, 
        split_nodes_link, 
        split_nodes_image, 
        extract_markdown_links, 
        extract_markdown_images, 
        text_to_textnodes)
from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_code,
        text_type_italic,
        text_type_image,
        text_type_link
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


    def test_split_images(self):
        node = TextNode("This sentence contains an image here: ![dog](https://doggy.com/somedog.png).", text_type_text)
        new_node = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode("This sentence contains an image here: ", text_type_text),
                    TextNode("dog", text_type_image,"https://doggy.com/somedog.png"),
                    TextNode(".", text_type_text)
                ],
                new_node)


    def test_split_images_two(self):
        node = TextNode("This has two image. The dog one ![dog](https://doggy.com/dog.png) and the cat one ![cat](https://cat.com/cat.png)", text_type_text)
        new_node = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This has two image. The dog one ", text_type_text),
                TextNode("dog", text_type_image, "https://doggy.com/dog.png"),
                TextNode(" and the cat one ", text_type_text),
                TextNode("cat", text_type_image, "https://cat.com/cat.png")
            ],
            new_node)


    def test_split_links(self):
        node = TextNode("This sentence contains an link here: [dog](https://doggy.com/somedog.png).", text_type_text)
        new_node = split_nodes_link([node])
        self.assertListEqual(
                [
                    TextNode("This sentence contains an link here: ", text_type_text),
                    TextNode("dog", text_type_link,"https://doggy.com/somedog.png"),
                    TextNode(".", text_type_text)
                ],
                new_node)


    def test_split_links_two(self):
        node = TextNode("This has two links. The dog one [dog](https://doggy.com/dog.png) and the cat one [cat](https://cat.com/cat.png)", text_type_text)
        new_node = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This has two links. The dog one ", text_type_text),
                TextNode("dog", text_type_link, "https://doggy.com/dog.png"),
                TextNode(" and the cat one ", text_type_text),
                TextNode("cat", text_type_link, "https://cat.com/cat.png")
            ],
            new_node)

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            nodes,
        )

