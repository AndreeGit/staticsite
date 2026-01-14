import unittest

from src.htmlnode import HtmlNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode("div", None, None, {"class": "test"})
        self.assertEqual(node.props_to_html(), " class=\"test\"")

    def test_to_html(self):
        node = HtmlNode("div", None, None, {"class": "test"})
        self.assertRaises(NotImplementedError)

    def test_repr(self):
        node = HtmlNode("div", None, None, {"class": "test"})
        self.assertEqual(repr(node), f'HtmlNode(div, None, None,  class="test")')

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "This is a headline")
        self.assertEqual(node.to_html(), "<h1>This is a headline</h1>")

    def test_leaf_to_html_h2(self):
        node = LeafNode("h2", "This is a headline")
        self.assertEqual(node.to_html(), "<h2>This is a headline</h2>")

    def test_leaf_to_html_without_value(self):
        node = LeafNode("br", None)
        self.assertRaises(ValueError)

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")

    def test_parent_to_html_without_children(self):
        node = ParentNode("div", None)
        self.assertRaises(ValueError)

    def test_parent_to_html_without_tag(self):
        node = ParentNode(None, [LeafNode("p", "Hello, world!")])
        self.assertRaises(ValueError)

    def test_parent_to_html_with_empty_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_parent_with_boot_example(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()