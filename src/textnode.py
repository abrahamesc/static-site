

class TextNode:
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


