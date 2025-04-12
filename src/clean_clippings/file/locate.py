import os

def locateDirectory(path):
	if not os.path.isdir(path):
		return False
	return True
		

def locateFile(path):
	if not os.path.isfile(path):
		return False
	return True
