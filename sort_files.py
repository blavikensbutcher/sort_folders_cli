import os
from helpers.is_folder_exist import is_folder_exist

image_extensions = [
    '.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi',  # JPEG
    '.png',                                             # PNG
    '.gif',                                             # GIF
    '.bmp', '.dib',                                     # BMP
    '.tiff', '.tif',                                    # TIFF
    '.svg', '.svgz',                                    # SVG
    '.webp',                                            # WebP
    '.ico', '.cur',                                     # ICO
    '.tga',                                             # TGA
    '.dds',                                             # DDS
    '.hdr', '.exr',                                     # HDR
    '.pbm', '.pgm', '.ppm',                             # PBM, PGM, PPM
    '.pnm', '.sr', '.ras', '.jp2', '.j2k', '.jpf',      # PNM, SR, RAS, JP2, J2K, JPF
    '.jpx', '.jpm', '.mj2',                             # JPX, JPM, MJ2
    '.heic', '.heif'                                    # HEIC, HEIF
]

documents_extensions = [
    '.pdf', '.doc', '.excel', '.txt',
]

music_extensions = ['.mp3', '.mp4', '.wav', '.aac']

archive_extensions = ['.rar', '.zip']

def sort(path):
    if not str(path).endswith("/"):
        path = path + "/"

    if not os.path.exists(path):
        print("Folder doesnt exists")
        return
    if not os.path.isdir(path):
        print("Path must be a folder")
        return

    # List of sorting folders
    image_folder_path = os.path.join(path, "images")
    archive_folder_path = os.path.join(path, "archives")
    music_folder_path = os.path.join(path, "music")
    documents_folder_path = os.path.join(path, "documents")
    unknownformat_folder_path = os.path.join(path, "unknownFormat")

    # List of all folders
    folders = []

    # List o all files
    files = []

    # List of sorted folders
    sorted_folders = [image_folder_path, archive_folder_path, music_folder_path, documents_folder_path, unknownformat_folder_path]

    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            folders.append(file)
        else:
            files.append(file)

    for file in files:
        # Making full path (path from arguments like /Users/User/Documents/Things/Filename.file
        full_path = os.path.join(path, file)
        # Making path to image folder like /Users/User/Documents/Things/Images
        # If folder doesn't exist create folder
        # We split name of file to check is it image or smth else
        splitted = os.path.splitext(file)
        # If extension in file equals image extension we move it to image
        if splitted[1] in image_extensions:
            # Check is folder exist if not -- create folder
            is_folder_exist(image_folder_path)
            # Create new path for image like /Users/User/Documents/Things/Images/Imagename.jpg
            new_path = os.path.join(image_folder_path, file)
            os.rename(full_path, new_path)
        elif splitted[1] in documents_extensions:
            is_folder_exist(documents_folder_path)
            new_path = os.path.join(documents_folder_path, file)
            os.rename(full_path, new_path)
        elif splitted[1] in music_extensions:
            is_folder_exist(music_folder_path)
            new_path = os.path.join(music_folder_path, file)
            os.rename(full_path, new_path)
        elif splitted[1] in archive_extensions:
            is_folder_exist(archive_folder_path)
            new_path = os.path.join(archive_folder_path, file)
            os.rename(full_path, new_path)
        else:
            is_folder_exist(unknownformat_folder_path)
            new_path = os.path.join(unknownformat_folder_path, file)
            os.rename(full_path, new_path)

    # for root, dirs, files in os.walk(path):