from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_bold
 )

def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        parts = node.text.split(delimeter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")

        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], text_type_text))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
