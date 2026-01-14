import unittest

from src.block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):

        self.assertEqual(block_to_block_type("# heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### heading"), BlockType.HEADING)
        # Ungültig: mehr als 6 oder fehlendes Leerzeichen
        self.assertEqual(block_to_block_type("####### heading"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#heading"), BlockType.PARAGRAPH)

    def test_code(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        # Ungültig: schließende Backticks fehlen oder falscher Start
        self.assertEqual(block_to_block_type("```\nhello"), BlockType.PARAGRAPH)

    def test_quote(self):
        block = "> This is a quote\n> with multiple lines"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        # Ungültig: eine Zeile hat kein >
        bad_block = "> Quote\nMissing symbol"
        self.assertEqual(block_to_block_type(bad_block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        # Ungültig: ein Sternchen statt Bindestrich (laut deiner Anforderung)
        bad_block = "- item 1\n* item 2"
        self.assertEqual(block_to_block_type(bad_block), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        # Ungültig: falsche Reihenfolge
        bad_order = "1. first\n3. second"
        self.assertEqual(block_to_block_type(bad_order), BlockType.PARAGRAPH)
        # Ungültig: startet nicht bei 1
        bad_start = "2. start\n3. next"
        self.assertEqual(block_to_block_type(bad_start), BlockType.PARAGRAPH)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just a normal text block."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
