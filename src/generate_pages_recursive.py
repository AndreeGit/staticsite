import os
from src.generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                dest_file_path = dest_path.replace(".md", ".html")
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                generate_page(from_path, template_path, dest_file_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
