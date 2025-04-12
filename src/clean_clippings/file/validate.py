import re
def validateFile(file):		
	with open(file, mode='r') as f:
		text = f.read()

		# Check that we have at least enough lines for a single highlight
		if len(text.splitlines()) < 5:
			return False
		
		text = text.replace("\ufeff", "").split("==========\n") # split up by dividing '=========='
		
		# if theres only one item in the list should still validate that item
		if len(text) == 1:
			lines = text[0].splitlines()
			if len(lines) != 4:
				return False
		
			if not re.match("^.* [(].*[)]", lines[0]) or not re.match(".* | Location [0-9]+-[0-9]+ | .*", lines[1]) or not re.match("", lines[2]) or not re.match(".*", lines[3]):
				return False
		# if theres more than one item in the list validate each
		else:
			for highlight in text[:-1]:
				lines = highlight.splitlines()
				if len(lines) != 4:
					return False

				if not re.match("^.* [(].*[)]", lines[0]) or not re.match(".* | Location [0-9]+-[0-9]+ | .*", lines[1]) or not re.match("", lines[2]) or not re.match(".*", lines[3]):
					return False
	
	# If all of the above runs well, then we know it's a valid clipping
	return True
