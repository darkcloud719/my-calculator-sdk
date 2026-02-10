from pathlib import Path

IGNORE_DIRS = [".venv",".git","__pycache__"]

def generate_tree(path: Path, prefix=""):
    lines = []
    entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    for i, entry in enumerate(entries):
        if entry.name in IGNORE_DIRS:
            continue
        print(f"Processing: {entry}")


        connector = "└─ " if i == len(entries) -1 else "├─ "
        lines.append(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():
            extension = "   " if i == len(entries) - 1 else "│  "
            lines.extend(generate_tree(entry, prefix + extension))
    return lines

root = Path(".")
tree_lines = generate_tree(root)

# with open("tree.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(tree_lines))

 