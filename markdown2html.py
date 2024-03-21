#!/usr/bin/python3
"""
It’s time to code a Markdown to HTML!
"""

import sys
from os import path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write(f'Usage: {sys.argv[0]} README.md README.html\n')
        exit(1)
    else:
        markDownFile = sys.argv[1]
        outputFile = sys.argv[2]
        if not path.exists(markDownFile):
            sys.stderr.write(f'Missing {markDownFile}\n')
            exit(1)
        else:
            exit(0)
