
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented here")

    def props_to_html(self):
        if self.props == None:
            return ""
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html

    def __repr__(self):
        return f'tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props} '


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):

        if self.value == None:
            raise ValueError("No value was provided")
        elif self.tag == None:
            return f'{self.value}' 
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


