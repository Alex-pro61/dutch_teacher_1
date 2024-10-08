import os

def generate_structure(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(dirpath)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in filenames:
            print(f'{subindent}{f}')

if __name__ == "__main__":
    generate_structure('.')
