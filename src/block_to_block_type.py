from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

"""
    Headings start with 1-6 # characters, followed by a space and then the heading text.
    Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks.
    Every line in a quote block must start with a "greater-than" character and a space: >
    Every line in an unordered list block must start with a - character, followed by a space.
    Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    If none of the above conditions are met, the block is a normal paragraph.
"""
def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    lines = block.split("\n")

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                break
        else:
            return BlockType.QUOTE

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                break
        else:
            return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        expected_number = 1
        for line in lines:
            if not line.startswith(f"{expected_number}. "):
                break
            expected_number += 1
        else:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH