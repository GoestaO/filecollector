import click
from collector import *

@click.group()
def collect():
    """
    To collect files in folders and subfolders with a certain file type
    """
    pass


@collect.command("show", help="Shows files in a directory with a given file type")
@click.option('--src', default=os.getcwd())
@click.option('--filetype', prompt=True, help="The filetype that should be used as filter.")
def show_filtered_files(src, filetype):
    all_files = findAllFiles(directory=src)
    filtered_files = filterFiles(filelist=all_files, filetype=filetype)
    click.echo(filtered_files)

# @collect.command("consolidate", help="Consolidates all files of a given file in a folder and its subfolders in one folder")
# def consolidate_files(src, filetype, dest)


if __name__ == '__main__':
    collect()