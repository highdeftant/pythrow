#!/bin/env python3

import os
import sys
import shututil

search_term = sys.argv[2]
folder = "/Volumes/LaCie"
raw_count = 0


def removeraw():
    for path, dirs, file in os.walk(folder, topdown=True):
        for dirname in dirs:
            if sys.argv[1] in dirname.lower():
                fullpath = os.path.join(path, dirname)
                print("Found: {full_path}")
                print("Removing {}...", fullpath)
                shututil.rmtree(fullpath)


if __name__ == "__main__":
    removeraw()
