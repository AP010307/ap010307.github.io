import os
import re

def convert_md_images_to_figure(root_dir="content"):
    pattern = r'!\[(.*?)\]\((.*?)\)'
    replacement = r'{{< figure src="\2" alt="\1" >}}'

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(subdir, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                new_content = re.sub(pattern, replacement, content)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

                print(f"✅ Updated: {file_path}")

convert_md_images_to_figure()
