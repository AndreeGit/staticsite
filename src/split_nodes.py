from src.extract_markdown import extract_markdown_images, extract_markdown_links
from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax: delimiter '{delimiter}' not closed in text: {node.text}")
        split_nodes = []
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def _split_nodes_base(old_nodes, extract_func, text_type, template):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        items = extract_func(node.text)
        if not items:
            new_nodes.append(node)
            continue

        current_text = node.text
        for alt_text, url in items:
            sections = current_text.split(template.format(alt_text, url), 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, text_type, url))
            current_text = sections[1]

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes


def split_nodes_image(old_nodes):
    return _split_nodes_base(old_nodes, extract_markdown_images, TextType.IMAGE, "![{}]({})")


def split_nodes_link(old_nodes):
    return _split_nodes_base(old_nodes, extract_markdown_links, TextType.LINK, "[{}]({})")

