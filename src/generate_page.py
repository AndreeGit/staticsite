from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file at from_path and store the contents in a variable.
    with open(from_path, 'r') as markdown_file:
        markdown_content = markdown_file.read()

    # Read the template file at template_path and store the contents in a variable
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    html = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)

    # Write the new full HTML page to a file at dest_path.
    # Be sure to create any necessary directories if they don't exist.
    with open(dest_path, 'w') as html_file:
        html_file.write(template_content)
