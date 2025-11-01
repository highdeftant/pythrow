#!/bin/env python3

import os
import sys
import shututil

search_term = sys.argv[2]
folder = "/Volumes/LaCie"
raw_count = 0


def removeraw():
    for path, dirname, filename in os.walk(folder, topdown=True):
        for dirname in dirnames:
            if "raw" in dirname.lower():
                full_path = os.path.join(dirpath, dirname)
                print(f"Found: {full_path}")


def check_dir(folders):
    folders = []
    for item in os.listdir(directory):
        try:
            if os.path.isdir(item):
                folders.append(item)
        except OSError as e:
            print("Error listing folder: {e}")

def checkraw(folders, term):
            for file in folders:
             if os.path.isfile(file):
                  if term in file:
                      try:
                          print("Removing RAW: {file}")
                          os.remove(filepath)
                          print("Removed: {file}")
                          raw_count += 1
                      except OSError as e:
                          print("Error Removing {file}: {e}")



def move_file(file):
    pass


if __name__ == "__main__":
    removeraw()
