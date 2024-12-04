import os
import shutil

# Define source and destination paths
source_path = './docs'
dest_path = './pages'

# Ensure destination exists
os.makedirs(dest_path, exist_ok=True)

# List all .md files and convert them to .mdx
for root, dirs, files in os.walk(source_path):
    for file in files:
        if file.endswith('.md'):
            md_file_path = os.path.join(root, file)
            mdx_file_path = os.path.join(dest_path, file.replace('.md', '.mdx'))
            # Simply copy the file content
            shutil.copyfile(md_file_path, mdx_file_path)