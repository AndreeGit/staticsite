from src.split_nodes import split_nodes_image, split_nodes_link, split_nodes_delimiter
from src.textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    delimiters = [
        ("**", TextType.BOLD),
        ("`", TextType.CODE),
        ("_", TextType.ITALIC),
    ]

    for delimiter, text_type in delimiters:
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)

    return nodes

