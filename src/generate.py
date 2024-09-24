from convert_tm import markdown_to_html_node
from markdown import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating {dest_path} from {from_path} and {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    html_nodes = markdown_to_html_node(markdown)
    title = extract_title(markdown)

    with open(template_path, "r") as f:
        template = f.read()
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_nodes.to_html())

    with open(dest_path, "w") as f:
        f.write(template)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for dirs in dirs:
            os.makedirs(os.path.join(dest_dir_path, os.path.relpath(root, dir_path_content), dirs), exist_ok=True)
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir_path, os.path.relpath(from_path, dir_path_content)).replace(".md", ".html")
                generate_page(from_path, template_path, dest_path)