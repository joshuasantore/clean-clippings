import os

def locateDirectory(path):
	if not os.path.isdir(path):
		raise NotADirectoryError(f"No directory found matching: '{path}'")

def locateFile(path):
	if not os.path.isfile(path):
		raise FileNotFoundError(f"No file found matching: '{path}' ")
