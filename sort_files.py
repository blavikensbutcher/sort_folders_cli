import os
import shutil
from helpers.is_folder_exist import is_folder_exist
from constants.file_extensions import music_extensions, image_extensions, documents_extensions, archive_extensions

sorting_folders = ['images', 'archives', 'music', 'documents', 'unknownFormat']


def sort_all_files(path):

    if not str(path).endswith("/"):
        path = path + "/"

    # List of sorting folders
    image_folder_path = os.path.join(path, "images")
    archive_folder_path = os.path.join(path, "archives")
    music_folder_path = os.path.join(path, "music")
    documents_folder_path = os.path.join(path, "documents")
    unknownformat_folder_path = os.path.join(path, "unknownFormat")


    for root, dirs, files in os.walk(path):
        for file in files:
            if str(file).endswith(music_extensions):
                new_path = os.path.join(music_folder_path, file)
                os.rename(os.path.join(root, file), new_path)
            elif str(file).endswith(documents_extensions):
                new_path = os.path.join(documents_folder_path, file)
                os.rename(os.path.join(root, file), new_path)
            elif str(file).endswith(archive_extensions):
                new_path = os.path.join(archive_folder_path, file)
                os.rename(os.path.join(root, file), new_path)
            elif str(file).endswith(image_extensions):
                new_path = os.path.join(image_folder_path, file)
                os.rename(os.path.join(root, file), new_path)


def delete_empty_folders(root):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            ds_store_exists = '.DS_Store' in filenames
            is_empty = not filenames and not dirnames
            if ds_store_exists and is_empty:
                print(f"Empty directory with .DS_Store removed: {dir_path}")
                shutil.rmtree(dir_path)
            elif is_empty:
                print(f"Empty directory removed: {dir_path}")
                shutil.rmtree(dir_path)
            else:
                delete_empty_folders(dir_path)

