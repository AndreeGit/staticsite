import unittest

from src.text_to_textnodes import text_to_textnodes
from src.textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )
        self.assertListEqual(nodes,
         [
             TextNode("This is ", TextType.TEXT),
             TextNode("text", TextType.BOLD),
             TextNode(" with an ", TextType.TEXT),
             TextNode("italic", TextType.ITALIC),
             TextNode(" word and a ", TextType.TEXT),
             TextNode("code block", TextType.CODE),
             TextNode(" and an ", TextType.TEXT),
             TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
             TextNode(" and a ", TextType.TEXT),
             TextNode("link", TextType.LINK, "https://boot.dev"),
         ]
        )

    def test_text_to_textnodes_plain(self):
        nodes = text_to_textnodes("This is just plain text")
        self.assertListEqual(nodes,
            [TextNode("This is just plain text", TextType.TEXT)]
        )

    def test_text_to_textnodes_multiple_bold(self):
        nodes = text_to_textnodes("This is **bold** and this is **also bold**")
        self.assertListEqual(nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and this is ", TextType.TEXT),
                TextNode("also bold", TextType.BOLD),
            ]
        )

    def test_text_to_textnodes_link_and_image(self):
        nodes = text_to_textnodes(
            "Check this [link](https://boot.dev) and ![image](https://img.png)"
        )
        self.assertListEqual(nodes,
            [
                TextNode("Check this ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.png"),
            ]
        )

    def test_text_to_textnodes_invalid_markdown(self):
        with self.assertRaises(ValueError):
            text_to_textnodes("This is **invalid bold")