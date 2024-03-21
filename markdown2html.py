#!/usr/bin/python3
"""
It’s time to code a Markdown to HTML!
"""

from sys import argv
from os import path

if __name__ == "__main__":
	if len(argv) < 3:
		print('Usage: ./markdown2html.py README.md README.html')
		exit(1)
	else:
		markDownFile = argv[1]
		outputFile = argv[2]
		if path.exists(markDownFile) is False:
			print('Missing ' + markDownFile)
			exit(1)
		else:
			exit(0)