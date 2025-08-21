import os.path


def update_text(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not exist!")
        return
    file = open(filename, "r")



    list_text = []
    for x in file.readlines(): #read each line and append to List_text
        list_text.append(x)

    list_text[0] = "Chapter 9 Data Structure dob"  # Update text in index = 0 of list to new text
    list_text[1] = "10.1-Introduction"  # Update text in index = 1 of list to new text

    i = 0
    while i < len(list_text):
        list_text[i] = str(list_text[i]).replace("dob","Date of birth")
        i += 1



    open_file_w = open("Readme.txt", "w")

    open_file_w.write("") # clear all text in file
    # open_file_w.write()
    open_file_a = open("Readme.txt", "a")

    for t in list_text:
        open_file_a.write(t+"\n") # write text from List_text
def read_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not exist")
        return
    file = open(filename, "r")
    print(file.readline())

def create_new_file(filename):
    if os.path.exists(filename):
        print(f"File {filename} already exist!")
        return
    open(filename, "x")



def append_file(filename, description):
    if not os.path.exists(filename):
        print(f"File {filename} not found! Creating file {filename}")
    f = open(filename, "a")
    f.write(description)
    print("Success!")


def write_file(filename, description):
    if not os.path.exists(filename):
        print(f"File {filename} not found! Creating file {filename}")
    f = open(filename, "w")
    f.write(description)
    print("Success!")

def clear_text(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not exist")
        return
    f = open(filename, "w")
    f.write("")
    print("Text is already clear")


