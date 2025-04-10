import click
from clean_clippings.file.locate import locateDirectory, locateFile 

@click.command()
@click.option('-d', '--dir', is_flag=True, help='path is to a directory')
@click.argument('path', nargs=-1, required=True)
def cli(dir: bool, path):
	if dir:
		for dir in path:
			locateDirectory(dir)
	else:
		for file in path:
			if file[-4:] != '.txt':
				raise ValueError("path must be to a .txt file unless -d flag provided")
			locateFile(file)
	
	

