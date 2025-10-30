"""
task3.py
By Nick Hlousek

Goal of this script is to print out all tags in a document using a soup strainer
"""

import sys
import os
from bs4 import BeautifulSoup, SoupStrainer

no_strainer = SoupStrainer()

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("USER ERROR\nEXECUTABLE STRUCTURE: python ./task3.py [HTML/XML File]")
        sys.exit()

    file_tree = None
    file_name = sys.argv[1]
    file_type = file_name.split('.')[-1]

    file_handle = open(file_name, "r")

    if (file_type == "html") or (file_type == "htm"):
        file_tree = BeautifulSoup(file_handle, "lxml", parse_only=no_strainer)
    elif (file_type == "xml"):
        file_tree = BeautifulSoup(file_handle, "xml", parse_only=no_strainer)
    else:
        print("NOT VALID FILE: Expecting file ending in 'htm', 'html', or 'xml'")
        sys.exit()

    file_handle.close()

    print(file_tree)

