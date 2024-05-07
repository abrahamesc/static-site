from htmlnode import LeafNode

text_type_text="text"
text_type_code="code"
text_type_bold="bold"
text_type_italic="italic"
text_type_image="image"
text_type_link="link"

class TextNode():
    def __init__(self, text, type, url=None):
        self.text = text
        self.type = type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.type == other.type and self.url == other.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.type == 'text':
        return LeafNode(None, text_node.text)

    if text_node.type == 'bold':
        return LeafNode('b', text_node.text)

    if text_node.type == 'italic':
        return LeafNode('i', text_node.text)

    if text_node.type == 'code':
        return LeafNode('code', text_node.text)

    if text_node.type == 'link':
        return LeafNode('a', text_node.text, {'href':text_node.url})

    if text_node.type == 'image':
        return LeafNode('img', "",{'src':text_node.url, 'alt':text_node.text} )


    

