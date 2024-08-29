# outline_directory.py - A program that displays the contents of a directory in a tree-like structure.
import os
import fnmatch

def list_files_and_folders(path, exclude=None, indent="", is_last=False):
    if exclude is None:
        exclude = []

    try:
        items = os.listdir(path)
    except PermissionError:
        print(indent + "└── " + "Permission Denied")
        return

    # Filter out the items that match any of the patterns in the exclude list
    items = [item for item in items if not any(fnmatch.fnmatch(item, pattern) for pattern in exclude)]
    items.sort(key=lambda x: (os.path.isfile(os.path.join(path, x)), x.lower()))

    for index, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_last_item = (index == len(items) - 1)
        connector = "└── " if is_last_item else "├── "
        print(indent + connector + item)

        if os.path.isdir(full_path):
            new_indent = indent + ("    " if is_last_item else "│   ")
            list_files_and_folders(full_path, exclude, new_indent, is_last_item)

if __name__ == "__main__":
    path = input("Enter the path: ").strip()

    if os.path.exists(path):
        exclude = []

        while True:
            # Allow the user to input files or patterns to exclude
            pattern = input("Enter a file or folder pattern to exclude (or press Enter to finish): ").strip()
            if not pattern:
                break
            exclude.append(pattern)

        print(f"\nExcluding: {exclude}\n")
        print(path)
        list_files_and_folders(path, exclude)
    else:
        print("The specified path does not exist.")

    input("Press Enter to exit.")
