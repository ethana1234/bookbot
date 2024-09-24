from generate import generate_page_recursive

def main():
    generate_page_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
