import unittest
from block_markdown import(
        block_to_block_type,
        block_type_code,
        block_type_quote,
        block_type_heading,
        block_type_ordered_list,
        block_type_unordered_list,
        block_type_paragraph,
        markdown_to_blocks)

class TestTextInline(unittest.TestCase):

    def test_code_block(self):
        code_block = '```\nprint("Hello World")\n```'
        code_type = block_to_block_type(code_block)
        self.assertEqual(code_type, block_type_code)

    def test_header_block(self):
        header = "### This is the main header"
        code_type = block_to_block_type(header)
        self.assertEqual(code_type, block_type_heading)

    def test_unordered_list_block(self):
        list = "- This is item one\n- This is item two\n- This is item three"
        code_type = block_to_block_type(list)
        self.assertEqual(code_type, block_type_unordered_list)

    def test_ordered_list(self):
        list = "1. one\n2. two\n3. three\n4. four"
        code_type = block_to_block_type(list)
        self.assertEqual(code_type, block_type_ordered_list)

    def test_quote_block(self):
        quote = ">This is a quote by someone"
        code_type = block_to_block_type(quote)
        self.assertEqual(code_type, block_type_quote)

    def test_paragraph_block(self):
        par = """This is just some random piece of words
        This is more words.
        So it should be a paragraph now."""
        code_type = block_to_block_type(par)
        self.assertEqual(code_type, block_type_paragraph)

