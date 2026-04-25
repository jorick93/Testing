import os
import argparse
import hashlib

def hash_file(filepath):
    """Returns the SHA-256 hash of the file."""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def compare_files(file1, file2):
    """Compares two files by their content."""
    return hash_file(file1) == hash_file(file2)

def compare_directories(dir1, dir2):
    """Compares two directories and prints the differences."""
    # Get relative paths for all files in both directories
    dir1_files = {os.path.relpath(os.path.join(dp, f), dir1) for dp, dn, fn in os.walk(dir1) for f in fn}
    dir2_files = {os.path.relpath(os.path.join(dp, f), dir2) for dp, dn, fn in os.walk(dir2) for f in fn}

    # Files only in dir1
    only_in_dir1 = dir1_files - dir2_files
    if only_in_dir1:
        print("Files only in", dir1)
        for file in sorted(only_in_dir1):
            print("  ", file)

    # Files only in dir2
    only_in_dir2 = dir2_files - dir1_files
    if only_in_dir2:
        print("Files only in", dir2)
        for file in sorted(only_in_dir2):
            print("  ", file)

    # Common files, compare their contents
    common_files = dir1_files & dir2_files
    differing_files = []
    for file in common_files:
        file1 = os.path.join(dir1, file)
        file2 = os.path.join(dir2, file)
        if not compare_files(file1, file2):
            differing_files.append(file)

    if differing_files:
        print("Files with different content:")
        for file in sorted(differing_files):
            print("  ", file)

    if not only_in_dir1 and not only_in_dir2 and not differing_files:
        print("Folders are identical.")

    # Compare directories structure
    dir1_dirs = {os.path.relpath(dp, dir1) for dp, dn, fn in os.walk(dir1)}
    dir2_dirs = {os.path.relpath(dp, dir2) for dp, dn, fn in os.walk(dir2)}

    only_in_dir1_dirs = dir1_dirs - dir2_dirs
    only_in_dir2_dirs = dir2_dirs - dir1_dirs

    if only_in_dir1_dirs:
        print("Directories only in", dir1)
        for directory in sorted(only_in_dir1_dirs):
            print("  ", directory)

    if only_in_dir2_dirs:
        print("Directories only in", dir2)
        for directory in sorted(only_in_dir2_dirs):
            print("  ", directory)

def main():
    parser = argparse.ArgumentParser(description="Compare two directories to check if they are identical and list the differences.")
    parser.add_argument('dir1', type=str, help='Path to the first directory.')
    parser.add_argument('dir2', type=str, help='Path to the second directory.')
    args = parser.parse_args()

    dir1 = args.dir1
    dir2 = args.dir2

    if not os.path.isdir(dir1):
        print(f"Error: {dir1} is not a valid directory.")
        return
    if not os.path.isdir(dir2):
        print(f"Error: {dir2} is not a valid directory.")
        return

    compare_directories(dir1, dir2)

if __name__ == "__main__":
    main()
