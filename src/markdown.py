import re

def extract_title(text):
    if text.startswith("# "):
        return text.split("\n")[0][2:]
    raise ValueError("No title found")

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def markdown_to_blocks(markdown_string):
    # Split by 2+ newlines, remove leading/trailing whitespace, and remove extra whitespace
    return [re.sub(r'\s{2,}', ' ', re.sub(r'^\s+|\s+$', '', s, flags=re.MULTILINE)) for s in re.split(r'\n\n', re.sub(r'\n{3,}', '\n\n', markdown_string)) if s]

def block_to_block_type(text):
    heading_pattern = re.compile(r'^(#{1,6})\s+.*$', re.MULTILINE)
    code_block_pattern = re.compile(r'```.*?```', re.DOTALL)
    quote_block_pattern = re.compile(r'^(>\s+.*)$', re.MULTILINE)
    unordered_list_pattern = re.compile(r'^(\*|-)\s+.*$', re.MULTILINE)
    ordered_list_pattern = re.compile(r'^\d+\.\s+.*$', re.MULTILINE)

    if heading_pattern.match(text):
        return 'Heading'
    elif code_block_pattern.match(text):
        return 'Code Block'
    elif all(quote_block_pattern.match(line) for line in text.split('\n')):
        return 'Quote Block'
    elif all(unordered_list_pattern.match(line) for line in text.split('\n')):
        return 'Unordered List Block'
    elif all(ordered_list_pattern.match(line) for line in text.split('\n')):
        return 'Ordered List Block'
    else:
        return 'Normal Paragraph'
