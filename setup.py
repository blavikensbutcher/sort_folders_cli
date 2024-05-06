from setuptools import setup

setup(
    name="sort_folders",
    version="0.1",
    description="Cleaning folder with script",
    url="https://github.com/blavikensbutcher/sort_folders_cli",
    author="Pidnebesnyi Volodymyr",
    author_email="luckertheory@gmail.com",
    license="MIT",
    packages=['sort_folders_cli'],
    long_description="Some long text",
    entry_points={
        'console_scripts': [
            'sort_all_files = sort_files:sort_all_files',
        ]
    }
)
