import sys
import sort_files


def main():
    if len(sys.argv) < 2:
        print("Введіть шлях до папки сортування")
    else:
        # Taking sorting path from command line
        sorting_folder = sys.argv[1]
        sort_files.sort_all_files(sorting_folder)
        sort_files.delete_empty_folders(sorting_folder)


if __name__ == '__main__':
    main()
