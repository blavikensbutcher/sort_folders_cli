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
                is_folder_exist(music_folder_path)
                os.rename(os.path.join(root, file), new_path)
            elif str(file).endswith(documents_extensions):
                new_path = os.path.join(documents_folder_path, file)
                is_folder_exist(documents_folder_path)
                os.rename(os.path.join(root, file), new_path)
            elif str(file).endswith(archive_extensions):
                new_path = os.path.join(archive_folder_path, file)
                is_folder_exist(archive_folder_path)
                os.rename(os.path.join(root, file), new_path)
            elif str(file).endswith(image_extensions):
                new_path = os.path.join(image_folder_path, file)
                is_folder_exist(image_folder_path)
                os.rename(os.path.join(root, file), new_path)
            else:
                new_path = os.path.join(unknownformat_folder_path, file)
                is_folder_exist(unknownformat_folder_path)
                os.rename(os.path.join(root, file), new_path)

    delete_empty_folders(path)


def delete_empty_folders(root):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        if not filenames and not dirnames:
            print(f"Empty directory removed: {dirpath}")
            shutil.rmtree(dirpath)

