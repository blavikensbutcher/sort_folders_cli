import os


def delete_empty_folders(path):
    for root, dirs, files in os.walk(path):
        if len(files) == 0 and len(dirs) == 0:
            print(f"Empty dir removed", root)
            if os.path.exists(root):
                os.rmdir(root)
        else:
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                delete_empty_folders(dir_path)