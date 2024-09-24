import unittest

from markdown import markdown_to_blocks, block_to_block_type
from convert_tm import markdown_to_html_node


class TestMarkdown(unittest.TestCase):
    def test_heading1(self):
        self.assertEqual(block_to_block_type("# Heading 1"), "Heading")

    def test_heading2(self):
        self.assertEqual(block_to_block_type("#### Heading 4"), "Heading")

    def test_codeblock1(self):
        self.assertEqual(block_to_block_type("```code block```"), "Code Block")

    def test_codeblock2(self):
        self.assertEqual(block_to_block_type("""```
more code block```"""), "Code Block")

    def test_quote(self):
        self.assertEqual(block_to_block_type("""> Quote block
> Quote block 2 ah"""), "Quote Block")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("""* list item 111
* list item 2 ah"""), "Unordered List Block")

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("""1. Ordered list item 1
2. Ordered list item 2ahhhh"""), "Ordered List Block")

    def test_text(self):
        self.assertEqual(block_to_block_type("Some text :)"), "Normal Paragraph")
      
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()