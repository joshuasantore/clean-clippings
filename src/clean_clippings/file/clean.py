'''
	Input Data

	`title (author lastname, author firstname)
	- Your Highlight on page X | Location X-X | Added on DAY, MONTH DATE, YEAR TIME am/pm

	content
	==========`

	Output Data

	`title
	author lastname, author firstname
	content`

'''

def cleanFile(file):
	highlights = []

	# Get all the data we want to keep from the file
	with open(file, mode='r', encoding='utf-8-sig') as f:
		text = f.read().replace("\ufeff", "").split("==========\n") # split up by dividing '=========='

		for highlight in text[0:-1]: # need to ignore the last blank line

			lines = highlight.split("\n") # split by line

			title_author = lines[0].split("(") # title and author on first line. after this step we have [title, "author lastname, author firstname)"]
			title = title_author[0]
			author = title_author[1][:-1]

			content = lines[3]	# content is on the third line by itself


			highlights.append({"title": title, "author": author, "content": content})

	cleanedHighlights = []

	# simple unoptimized procedure to remove any duplicates
	for i in range(len(highlights)):
		subhighlight = False
		for j in range(len(highlights)):
			if highlights[i]['content'] in highlights[j]['content'] and i != j:
				subhighlight = True
		if subhighlight == False:
			cleanedHighlights.append(highlights[i])

	# Write the highlights back to the file replacing what was there
	with open(file, mode='w+', encoding='utf-8') as f:
		for highlight in cleanedHighlights:
			f.writelines(highlight['title']+'\n')
			f.writelines(highlight['author']+'\n')
			f.writelines(highlight['content']+'\n\n')

	

