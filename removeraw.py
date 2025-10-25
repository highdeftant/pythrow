#!/bin/env python3

import os

folder = "/home/gh0st/Documents"
#folder = "/Volumes/LaCie"

def checkraw(directory, term):
    for file in os.listdir(directory):
         if os.path.isfile(file):
             if term in file:
                 try:
                     os.remove(filepath)
                     print("Removed: {filepath}")
                 except OSError as e:
                     print("Error Removing {filepath}: {e}")

if __name__ == "__main__":

    print("Searching for RAW files....")
    checkraw(folder, "raw")
