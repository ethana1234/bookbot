from markdown import markdown_to_blocks, block_to_block_type
from textnode import text_to_textnodes
from htmlnode import ParentNode, LeafNode, text_node_to_html


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode(children, tag="div")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html(text_node)
        children.append(html_node)
    return children

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case "Heading":
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            if level + 1 >= len(block):
                raise ValueError(f"Invalid heading level: {level}")
            text = block[level + 1 :]
            children = text_to_children(text)
            return ParentNode(children, tag=f"h{level}")
        case "Normal Paragraph":
            return ParentNode(text_to_children(block), "p")
        case "Unordered List Block":
            items = block.split("\n")
            html_items = []
            for item in items:
                text = item[2:]
                children = text_to_children(text)
                html_items.append(ParentNode(children, "li"))
            return ParentNode(html_items, tag="ul")
        case "Ordered List Block":
            items = block.split("\n")
            html_items = []
            for item in items:
                text = item[3:]
                children = text_to_children(text)
                html_items.append(ParentNode(children, "li"))
            return ParentNode(html_items, tag="ol")
        case "Code Block":
            if not block.startswith("```") or not block.endswith("```"):
                raise ValueError("Invalid code block")
            text = block[4:-3]
            children = text_to_children(text)
            return ParentNode(children, tag="code")
        case "Quote Block":
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                if not line.startswith(">"):
                    raise ValueError("Invalid quote block")
                new_lines.append(line.lstrip(">").strip())
            content = " ".join(new_lines)
            children = text_to_children(content)
            return ParentNode(children, tag="blockquote")
        case _:
            raise ValueError(f"Unknown block type: {block_type}")
        
if __name__ == "__main__":
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

    node = markdown_to_html_node(md)
    print(node.to_html())