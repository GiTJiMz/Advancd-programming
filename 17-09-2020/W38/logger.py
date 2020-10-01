#!/usr/bin/env python3
import sys
from datetime import datetime

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


def logger(file):
    def inner(msg, level="INFO"):
        print(f"{datetime.now()} - {level:^6} - {msg}", file=file)
    return inner

with open("testfile.txt", "w") as f:
    log = logger(f); 

    log("Hello, World!")
    log("Second log", level="DEBUG")

# 1. Make sure that the log prints the 'msg'

# 2. Include the info level

# 3. Also add a timestamp

# 4. Make sure you print to the file.
