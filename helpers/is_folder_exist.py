import os


def is_folder_exist(pathtofolder):
    if not (os.path.exists(pathtofolder)):
        os.mkdir(pathtofolder)
