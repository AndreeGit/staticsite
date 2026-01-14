from src.block_to_block_type import block_to_block_type, BlockType
from src.markdown_to_blocks import markdown_to_blocks
from src.htmlnode import HtmlNode, ParentNode, LeafNode
from src.text_to_textnodes import text_to_textnodes
from src.textnode import text_node_to_html_node


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            # Jede Zeile einzeln strippen, leere Zeilen entfernen und dann mit Leerzeichen joinen
            lines = block.split("\n")
            content = " ".join([line.strip() for line in lines])
            children = text_to_children(content)
            block_nodes.append(ParentNode("p", children))
        elif block_type == BlockType.HEADING:
            # Heading: Level zählen und Text extrahieren
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            if level + 1 >= len(block):
                raise ValueError(f"Invalid heading level: {level}")

            content = block[level + 1:]
            children = text_to_children(content)
            block_nodes.append(ParentNode(f"h{level}", children))

        elif block_type == BlockType.CODE:
            # Wir entfernen die einleitenden und abschließenden ```
            # Und geben den Inhalt als LeafNode (Text) zurück
            content = block[3:-3].strip("\n")
            code_node = ParentNode("code", [LeafNode(None, content + "\n")])
            block_nodes.append(ParentNode("pre", [code_node]))

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                # Wir schneiden "- " ab
                content = line[2:]
                children = text_to_children(content)
                list_items.append(ParentNode("li", children))
            block_nodes.append(ParentNode("ul", list_items))

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                # Bei "1. Item" müssen wir alles vor dem ersten Leerzeichen + Leerzeichen entfernen
                # Da die Zahl variieren kann (10. ), splitten wir am ersten Leerzeichen
                content = line.split(" ", 1)[1]
                children = text_to_children(content)
                list_items.append(ParentNode("li", children))
            block_nodes.append(ParentNode("ol", list_items))

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                if line.startswith("> "):
                    new_lines.append(line[2:])
                elif line.startswith(">"):
                    new_lines.append(line[1:])
                else:
                    new_lines.append(line)
            content = " ".join(new_lines)
            children = text_to_children(content)
            block_nodes.append(ParentNode("blockquote", children))

    return ParentNode("div", block_nodes)

