import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
import pathlib

# Recursively find all .py files
py_files = list(pathlib.Path(".").rglob("*.py"))

# Sort by path (optional)
py_files.sort()

# Build notebook cells
cells = []
for file_path in py_files:
    relative_path = str(file_path)
    
    # Add markdown cell with file path
    cells.append(new_markdown_cell(f"### `{relative_path}`"))
    
    # Add code cell with file content
    code = file_path.read_text(encoding='utf-8')
    cells.append(new_code_cell(code))

# Create notebook
nb = new_notebook(cells=cells)

# Save to .ipynb
with open("combined_files.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
