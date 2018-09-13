#generator_demo.py

import os

def gen_func():
    #Example: Generator Functions

    def filtered_text(text_lines,wanted_text):
        """ Compares each line in text_lines to wanted_text
            Yields the line if it matches """
        for line in text_lines:
            if wanted_text in line:
                yield line

    #slow method - read whole file into memory, then use the generator to filter text
    #need to wait for the whole file to load before anything else can begin
    #uses more memory
    #not much benefit here!
    with open("Programming_Books_List.txt",'r') as file_obj:
        lots_of_text = file_obj.readlines()
    matches = filtered_text(lots_of_text,"Python")
    for match in matches:
        print(match)

    #faster method - use the file object as an iterator, filter it with the generator
    #only needs to keep current line in memory
    #current line is only read directly before use
    #outputs each match directly after it is found (before the file has finished reading)
    with open("Programming_Books_List.txt",'r') as file_obj:
        matches = filtered_text(file_obj,"Python")
        for match in matches:
            print(match)

    #sleeker method - this is doing the same as the faster method above, but in fewer lines of code
    #instead of storing the generator object in a variable, it is immediately used in a for loop
    #this is perhaps less readable, so it can be harder to debug
    with open("Programming_Books_List.txt",'r') as file_obj:
        for match in filtered_text(file_obj,"Python"):
            print(match)

def gen_expr():
    #Example: Generator Expressions

    with open("Programming_Books_List.txt",'r') as file_obj:
        for match in (line for line in file_obj if "Python" in line):
            print(match)

#change to the examples folder
os.chdir("examples")
# gen_func()
gen_expr()