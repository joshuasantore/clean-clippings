# Clean Clippings

Designed to be something of a helper for my much larger "brain".

Essentially, I needed to be able to take the clippings.txt file from my amazon kindle, which holds all of my highlights from any given text, and remove all duplicate data as well as reformat the lines such that I can use the new file for bulk insertion of the aforementioned highlights into a database.

I packaged this functionality  into a command line application so that I could use it from anywhere in the terminal with ```clean-clippings "file"``` and instantly have the old clippings.txt file rewritten with the formatted data

## Usage

1. Clone from the repo
2. cd into the directory
3. ```pip install .```
2. ```clean-clippings [file]``` from anywhere on the system
