#!/usr/bin/python3
"""
It’s time to code a Markdown to HTML!
"""

import sys
from os import path

if __name__ == "__main__":

    def readHashTag(line, target="#"):
        """
        counts the amount of times a symbol (default = '#') occurs in a line
        Args:
                line (str): the particular line to be read
                target (str): the targeted symbol
        Return:
                hashCount (int): amount of hashtag found
        """
        hashCount = 0
        for char in line:
            if char == target:
                hashCount += 1
            else:
                break
        return hashCount

    def unorderedListTag(lines, target='-'):
        """
        Checks the line for the hyphen symbol ('-') and
        modify the input to reflect a HTML unordered list
        Args:
                line (str): the particular line to be read
        Return:
                unorderedList (str): formatted string
        """
        unorderedList = f'<ul>\n'
        for line in lines:
            if line.startswith(target):
                unorderedList += f'\t<li>{line[1:].strip()}</li>\n'
            else:
                break
        unorderedList += f'</ul>'
        return unorderedList
    
    def orderedListTag(lines, target='*'):
        """
        Checks the line for the hyphen symbol ('-') and
        modify the input to reflect a HTML ordered list
        Args:
                line (str): the particular line to be read
        Return:
                orderedList (str): formatted string
        """
        orderedList = f'<ol>\n'
        for line in lines:
            if line.startswith(target):
                orderedList += f'\t<li>{line[1:].strip()}</li>\n'
            else:
                break
        orderedList += f'</ol>'
        return orderedList

    if len(sys.argv) < 3:
        sys.stderr.write(f'Usage: {sys.argv[0]} README.md README.html\n')
        exit(1)
    else:
        markDownFile = sys.argv[1]
        outputFile = sys.argv[2]
        if not path.exists(markDownFile):
            sys.stderr.write(f'Missing {markDownFile}\n')
            exit(1)

        with open(markDownFile, 'r') as md, open(outputFile, 'w') as html:
            lines = md.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line.startswith("#"):
                    count = readHashTag(line)
                    content = line[count:].strip()
                    html.write(f"<h{count}>{content}</h{count}>\n")
                elif line.startswith("-"):
                    listLines = []
                    while i < len(lines) and lines[i].startswith("-"):
                        listLines.append(lines[i])
                        i += 1
                    i -= 1
                    html.write(unorderedListTag(listLines))
                elif line.startswith("*"):
                    listLines = []
                    while i < len(lines) and lines[i].startswith("*"):
                        listLines.append(lines[i])
                        i += 1
                    i -= 1
                    html.write(orderedListTag(listLines))
                else:
                    html.write(line + '\n')
                i += 1
        exit(0)
