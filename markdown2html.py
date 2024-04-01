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
            for readLine in md:
                count = readHashTag(readLine)
                if count > 0:
                    html.write(f"<h{count}>{readLine.strip()[count:].strip()}</h{count}>\n")
                else:
                    html.write(readLine)
        exit(0)