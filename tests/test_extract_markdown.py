import unittest
from src.extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
            matches
        )

    def test_extract_markdown_images_none(self):
        text = "This is text with no images"
        matches = extract_markdown_images(text)
        self.assertEqual([], matches)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
            matches
        )

    def test_extract_markdown_links_none(self):
        text = "This is text with no links"
        matches = extract_markdown_links(text)
        self.assertEqual([], matches)

    def test_extract_markdown_links_with_image(self):
        text = "This is a link [home](https://home.com) and an image ![alt](https://image.com/img.png)"
        matches = extract_markdown_links(text)
        self.assertEqual([("home", "https://home.com")], matches)

    def test_extract_markdown_images_with_link(self):
        text = "This is a link [home](https://home.com) and an image ![alt](https://image.com/img.png)"
        matches = extract_markdown_images(text)
        self.assertEqual([("alt", "https://image.com/img.png")], matches)

if __name__ == "__main__":
    unittest.main()
