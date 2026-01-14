import unittest

from src.markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings(self):
        md = """
# This is an h1

### This is an h3 with **bold**

###### This is an h6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()

        expected = (
            "<div>"
            "<h1>This is an h1</h1>"
            "<h3>This is an h3 with <b>bold</b></h3>"
            "<h6>This is an h6</h6>"
            "</div>"
        )
        self.assertEqual(html, expected)

    def test_codeblock(self):
        md = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_code_block(self):
        md = "```\nprint('hello world')\ndef logic():\n    return True\n```"

        node = markdown_to_html_node(md)
        html = node.to_html()

        expected = (
            "<div>"
            "<pre><code>print('hello world')\ndef logic():\n    return True\n</code></pre>"
            "</div>"
        )
        self.assertEqual(html, expected)

    def test_unordered_list(self):
        md = """
- first item
- second item with **bold**
"""
        node = markdown_to_html_node(md.strip())
        html = node.to_html()

        expected = (
            "<div><ul>"
            "<li>first item</li>"
            "<li>second item with <b>bold</b></li>"
            "</ul></div>"
        )
        self.assertEqual(html, expected)

    def test_ordered_list(self):
        md = """
1. first
2. second
"""
        node = markdown_to_html_node(md.strip())
        html = node.to_html()

        expected = (
            "<div><ol>"
            "<li>first</li>"
            "<li>second</li>"
            "</ol></div>"
        )
        self.assertEqual(html, expected)

    def test_quote_block(self):
        md = """
> This is a quote
> with multiple lines
"""
        node = markdown_to_html_node(md.strip())
        html = node.to_html()

        expected = (
            "<div><blockquote>This is a quote with multiple lines</blockquote></div>"
        )
        self.assertEqual(html, expected)

    def test_single_line_code_block(self):
        md = "```ls```"
        node = markdown_to_html_node(md)
        html = node.to_html()
        # Einzeiliger Code-Block sollte als Code-Block erkannt werden
        # Beachte: Mein aktueller block_to_block_type erkennt das nicht.
        # Und markdown_to_html_node geht davon aus, dass die Backticks in eigenen Zeilen stehen.
        # Das müssen wir eventuell anpassen.
        self.assertTrue("<pre><code>" in html)