"""
task1.py
By Nick Hlousek

Goal of this program is to read an HTML/XML File into a tree and write the
tree back onto the disk as a prettyfied file.
"""

import sys
import os
from bs4 import BeautifulSoup

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("USER ERROR\nEXECUTABLE STRUCTURE: python ./task1.py [HTML/XML File]")
        sys.exit()

    file_tree = None
    file_name = sys.argv[1]
    file_type = file_name.split('.')[-1]

    file_handle = open(file_name, "r")

    if (file_type == "html") or (file_type == "htm"):
        file_tree = BeautifulSoup(file_handle, "lxml")
    elif (file_type == "xml"):
        file_tree = BeautifulSoup(file_handle, "xml")
    else:
        print("NOT VALID FILE: Expecting file ending in 'htm', 'html', or 'xml'")
        sys.exit()
    
    pretty_filename = file_name + ".task1"

    if os.path.exists(pretty_filename):
        os.remove(pretty_filename)

    with open(pretty_filename, "w") as pretty_file:
        pretty_file.write(file_tree.prettify())

