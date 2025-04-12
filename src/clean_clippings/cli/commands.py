import click
import os
from clean_clippings.file.validate import validateFile
from clean_clippings.file.clean import cleanFile

@click.command()
@click.option('-d', '--dir', is_flag=True, help='path is to a directory')
@click.argument('path', nargs=-1, required=True)
def cli(dir: bool, path):
	if dir:
		# validate dirs
		for dir in path:
			if not os.path.isdir(dir):
				raise NotADirectoryError(f"directory {dir} does not exist")
			
	else:
		# validate files
		for file in path:
			if file[-4:] != '.txt':
				raise ValueError("path must be to a .txt file unless -d flag provided")
			
			if not os.path.isfile(file):
				raise FileNotFoundError(f"file {file} does not exist")
			
			if not validateFile(file):
				raise ValueError(f"file {file} is not formatted as a clippings.txt")

		# Clean each file once all are validated
		for file in path:
			cleanFile(file)

