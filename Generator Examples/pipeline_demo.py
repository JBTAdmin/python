#pipeline_demo.py

#Example: Search for "# TODO:" at start of lines in Python
# files, to pick up what I need to work on next
import os

def print_filenames(filenames):
    """Prints out each filename, and returns it back to the pipeline"""
    for filename in filenames:
        print(filename)
        yield filename

def file_read_lines(filenames):
    """Read every line from every file"""
    for filename in filenames:
        with open(filename,'r') as file_obj:
            for line in file_obj:
                yield line
#change to the examples folder
os.chdir("examples")
#get a list of all python files in this directory
filenames_list = os.listdir(".")
#turn it into a generator
filenames = (filename for filename in filenames_list)
#filter to only Python files (*.py)
filenames = (filename for filename in filenames if filename.lower().endswith(".py"))
#print out current file name, then pop it back into the pipeline
filenames = print_filenames(filenames)
#pass the filenames into the file reader, get back the file contents
file_lines = file_read_lines(filenames)
#strip out leading spaces and tabs from the lines
file_lines = (line.lstrip(" \t") for line in file_lines)
#filter to just lines starting with "# TODO:"
filtered = (line for line in file_lines if line.startswith("# TODO:"))
#strip out trailing spaces, tabs and newlines
filtered = (line.rstrip() for line in filtered)
#display output
for item in filtered:
    print(item)

# TODO: Write generator example
# TODO: Test on current folder
    # TODO: Test on a line indented with spaces
	# TODO: Test on a line indented with tabs
# TODO: Add more TODOs
