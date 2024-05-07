import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_bold,
    text_type_image
 )


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            print(f'This is original_text {original_text}')
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
            print(f'This is original_text after section[1] {sections[1]}')
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes    


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_images(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            print(f'This is original_text {original_text}')
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    link[0],
                    text_type_image,
                    link[1],
                )
            )
            original_text = sections[1]
            print(f'This is original_text after section[1] {sections[1]}')
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes    


