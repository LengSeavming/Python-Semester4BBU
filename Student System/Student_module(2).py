    # -create_new_file
    # -write_file_mode_a
    # -write_file_mode_w
    # -read_text
    # -read_texts

import os.path
import json

def read_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not exist")
        return
    file = open(filename, "r")
    print(file.readline())
    print("Success!")

def create_new_file(filename):
    if os.path.exists(filename):
        print(f"File {filename} already exist!")
        return
    open(filename, "x")

def create_new_file():
    print("Success!")

def write_file_mode_a():
    print("Success")

def write_file_mode_w():
    print("Success")

def read_text():
    print("Success")

def read_texts():
    print("Success")