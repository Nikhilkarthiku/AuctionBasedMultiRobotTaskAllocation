import os
from typing import List

class PythonFileReaderAgent:
    def __init__(self, root_dir,output_path):
        self.root_dir = root_dir
        self.output_path = output_path

    def read_python_files(self) -> List[str]:
        content = []
        for root, _, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith('.py'):
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content.append(f.read())
        return content

    def write(self, author: str, summary: str):
            with open(self.output_path, 'w', encoding='utf-8') as file:
                file.write(f"Author(s): {author}\n")
                file.write("\nSummary:\n")
                file.write(summary)

