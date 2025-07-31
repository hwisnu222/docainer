import sys
import os
import shutil


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def copy_other_files(src_dir, dest_dir, exclude_exts=(".j2",)):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if not file.endswith(exclude_exts):
                src_file = os.path.join(root, file)
                rel_path = os.path.relpath(src_file, src_dir)
                dest_file = os.path.join(dest_dir, rel_path)

                os.makedirs(os.path.dirname(dest_file), exist_ok=True)

                shutil.copy2(src_file, dest_file)
                print(f"Copied {rel_path}")
