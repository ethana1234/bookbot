import re

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    offset = len(delimiter)
    for node in old_nodes:
        text = node.text
        if delimiter not in text:
            new_nodes.append(node)
            continue
        while delimiter in text:
            start_index = text.index(delimiter)
            end_index = text.index(delimiter, start_index + 1)
            new_nodes += [TextNode(text[:start_index], "text"), TextNode(text[start_index+offset:end_index], text_type)]
            text = text[end_index+offset:]
        else:
            if text:
                new_nodes.append(TextNode(text, "text"))
    return new_nodes

def split_nodes_regex(old_nodes, pattern, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        parts = re.split(pattern, node.text)
        for part in parts:
            if not part:
                continue
            match = re.match(pattern, part)
            if match:
                text, url = re.findall(r'\[(.*?)\]\((.*?)\)', part)[0]
                new_nodes.append(TextNode(text, text_type, url))
            else:
                new_nodes.append(TextNode(part, "text"))
    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes_regex(old_nodes, r"(!\[.*?\]\(.*?\))", "image")

def split_nodes_link(old_nodes):
    return split_nodes_regex(old_nodes, r"(?<!!)(\[.*?\]\(.*?\))", "link")

def text_to_textnodes(text):
    return split_nodes_delimiter(
        split_nodes_delimiter(
            split_nodes_delimiter(
                split_nodes_image(
                    split_nodes_link(
                        [TextNode(text, "text")]
                    )
                ),
                "**",
                "bold"
            ),
            "*",
            "italic"
        ),
        "`",
        "code"
    )


#print(split_nodes_delimiter([TextNode("This is **text** with an *italic* word", "text")], "**", "bold"))
#print(text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))
