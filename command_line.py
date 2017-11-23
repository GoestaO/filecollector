import click
from collector import *

@click.group()
def collect():
    """
    A tool to deal with files in folders and subfolders
    """
    pass


@collect.command("show", help="Shows files in a directory/subdirectory with a given file type")
@click.option('--src', help="The folder that should be investigated. Default is the current directory.", default=os.getcwd(), type=click.Path(exists=True))
@click.option('--filetype', prompt=True, help="The filetype that should be used as filter.")
def show_filtered_files(src, filetype):
    all_files = findAllFiles(directory=src)
    filtered_files = filterFiles(filelist=all_files, filetype=filetype)
    click.echo("#################################################################################################################### \n")
    click.echo(filtered_files)

@collect.command("consolidate", help="Consolidates all files of a folder & subfolders with a given file in a folder in one place.")
@click.option('--src', help="The folder that should be investigated. Default is the current directory.", default=os.getcwd(), type=click.Path(exists=True))
@click.option('--filetype', prompt=True, help="The filetype that should be used as filter.")
@click.option('--dest', prompt=True, help="The folder that should contain the consolidated files")
def consolidate_files(src, filetype, dest):
    all_files = findAllFiles(directory=src)
    filtered_files = filterFiles(filelist=all_files, filetype=filetype)
    copyFiles(filtered_files, destination=dest)
    click.echo("#################################################################################################################### \n")
    click.echo("{0} files copied to {1}".format(len(filtered_files), dest))


if __name__ == '__main__':
    collect()