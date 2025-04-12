import os
from clean_clippings.file.validate import validateFile 

def locateValidFiles(dir):
	paths=[]
	files = os.listdir(dir)
	
	for file in files:
		path = os.path.join(dir,file)
		if path[-4:] == '.txt' and validateFile(path):
			paths.append(path)
	
	return paths

