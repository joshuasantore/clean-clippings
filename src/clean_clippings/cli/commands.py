import click

@click.command()
@click.option('-d', '--dir', is_flag=True, help='path is to a directory')
@click.argument('path', nargs=-1)
def cli(dir: bool, path):
	print(path)

