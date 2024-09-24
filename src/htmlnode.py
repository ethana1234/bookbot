class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value if value is not None else ""
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or self.children is None:
            raise ValueError("Need a tag and children to convert to HTML")
        return f"<{self.tag}{" ".join([f'{key}=\"{value}\"' for key, value in self.props.items()])}>{''.join(c.to_html() for c in self.children)}</{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        value = value.replace("\n", " ")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Need a value to convert to HTML")
        if self.tag is None:
            return self.value
        props_txt = " " + " ".join([f'{key}=\"{value}\"' for key, value in self.props.items()]) if self.props else ""
        return f"<{self.tag}{props_txt}>{self.value}</{self.tag}>"

def text_node_to_html(node):
    match node.text_type:
        case "text":
            return LeafNode(value=node.text)
        case "bold":
            return LeafNode(tag="b", value=node.text)
        case "italic":
            return LeafNode(tag="i", value=node.text)
        case "code":
            return LeafNode(tag="code", value=node.text)
        case "link":
            return LeafNode(tag="a", value=node.text, props={"href": node.url})
        case "image":
            return LeafNode(tag="img", props={"src": node.url, "alt": node.text}, value="")