import os
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Batch Symbolic Linking')
    parser.add_argument('--src_dir', type=str, help='source directory')
    parser.add_argument('--dst_dir', type=str, help='destination directory')
    parser.add_argument('--begin_file', type=str, help='first file in range')
    parser.add_argument('--end_file', type=str, help='last file in range')
    args = parser.parse_args()

    source_dir = os.path.abspath(args.src_dir)
    dest_dir = os.path.abspath(args.dst_dir)
    begin_file = args.begin_file
    end_file = args.end_file

    files = os.listdir(source_dir)
    files.sort()

    for f in files:
        if f >= begin_file and f <= end_file:
            file_source_path = os.path.join(source_dir, f)
            file_dest_path = os.path.join(dest_dir, f)
            print("Linking "+file_source_path+" to "+file_dest_path)
            os.symlink(file_source_path, file_dest_path)
