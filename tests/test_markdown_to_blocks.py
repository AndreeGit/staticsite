import unittest

from src.markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_multiple_newlines(self):
        md = """
    This is block 1


    This is block 2
"""
        # Testet, ob mehr als zwei Newlines zu leeren Blöcken führen
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            ["This is block 1", "This is block 2"]
        )

    def test_markdown_to_blocks_excessive_whitespace(self):
        md = """
      This block has leading and trailing whitespace   

      Another block with spaces  
    """
        # Testet, ob strip() korrekt auf jeden Block angewendet wird
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            ["This block has leading and trailing whitespace", "Another block with spaces"]
        )

    def test_markdown_to_blocks_empty_input(self):
        # Testet den Grenzfall eines komplett leeren Strings
        md = ""
        blocks = markdown_to_blocks(md)
        # Sollte entweder eine leere Liste zurückgeben oder wir filtern leere Strings aus
        self.assertListEqual(blocks, [])

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)

        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\n"
            "This is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]

        self.assertEqual(blocks, expected)
