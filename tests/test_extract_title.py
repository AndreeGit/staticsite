import unittest

from src.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# Hello")
        self.assertEqual(title, "Hello")

    def test_extract_title_no_heading(self):
        with self.assertRaises(ValueError):
            extract_title("No heading here")

    def test_extract_title_multiline(self):
        markdown = """
This is a paragraph.

# The Real Title

Another paragraph.
"""
        title = extract_title(markdown)
        self.assertEqual(title, "The Real Title")

    def test_extract_title_with_whitespace(self):
        title = extract_title("#   Hello   ")
        self.assertEqual(title, "Hello")

    def test_extract_title_wrong_level(self):
        with self.assertRaises(ValueError):
            extract_title("## Secondary Title")

    def test_extract_title_no_space(self):
        with self.assertRaises(ValueError):
            extract_title("#NoSpaceAfterHash")
            
    