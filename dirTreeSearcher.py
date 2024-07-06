import os
import argparse
from datetime import datetime

def list_files(startpath, indent='', depth=None, file_filter=None, search=None):
    if not os.path.isdir(startpath):
        return

    files = os.listdir(startpath)
    files.sort()

    for i, file in enumerate(files):
        full_path = os.path.join(startpath, file)
        is_last = (i == len(files) - 1)

        if os.path.isdir(full_path):
            print(f"{indent}\033[34m├── {file}/\033[0m")
            if depth is None or depth > 0:
                new_indent = indent + ('    ' if is_last else '│   ')
                new_depth = None if depth is None else depth - 1
                list_files(full_path, new_indent, new_depth, file_filter, search)
        else:
            if file_filter and not file.endswith(file_filter):
                continue
            if search and search not in file:
                continue
            mod_time = datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M:%S')
            if is_last:
                print(f"{indent}\033[32m└── {file} \033[33m[{mod_time}]\033[0m")
            else:
                print(f"{indent}\033[32m├── {file} \033[33m[{mod_time}]\033[0m")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List files in a directory in tree form.")
    parser.add_argument("startpath", type=str, help="The root directory to start listing from.")
    parser.add_argument("-d", "--depth", type=int, default=None, help="Maximum depth of recursion.")
    parser.add_argument("-f", "--filter", type=str, default=None, help="File extension filter (e.g. '.txt').")
    parser.add_argument("-o", "--output", type=str, default=None, help="Output file to save the tree structure.")
    parser.add_argument("-s", "--search", type=str, default=None, help="Search for a specific file name.")

    args = parser.parse_args()

    # Debugging output
    print(f"Arguments: {args}")

    output = []
    def capture_output(text):
        output.append(text)

    # Redirect print to capture_output if output file is specified
    if args.output:
        import sys
        sys.stdout = type('stdout', (object,), {'write': capture_output})()

    list_files(args.startpath, '│   ', args.depth, args.filter, args.search)

    # Write to file if output file is specified
    if args.output:
        with open(args.output, 'w') as f:
            f.write('\n'.join(output))
