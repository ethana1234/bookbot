import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        node = TextNode("This is a text node", "italic", url="https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", url="https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is NOT a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
        node = TextNode("This is a text node", "bold", url="https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
        node = TextNode("This is a text node", "bold", url="https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", url="https://www.boot.dev")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()