"""
task2.py
By Nick Hlousek

Goal of this program is to print all the hyperlinks (<a> tags) in the file using a SoupStrainer
"""

import sys
import os
from bs4 import BeautifulSoup, SoupStrainer

hyperlink_strainer = SoupStrainer('a')

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("USER ERROR\nEXECUTABLE STRUCTURE: python ./task2.py [HTML/XML File]")
        sys.exit()

    file_tree = None
    file_name = sys.argv[1]
    file_type = file_name.split('.')[-1]

    file_handle = open(file_name, "r")

    if (file_type == "html") or (file_type == "htm"):
        file_tree = BeautifulSoup(file_handle, "lxml", parse_only=hyperlink_strainer)
    elif (file_type == "xml"):
        file_tree = BeautifulSoup(file_handle, "xml", parse_only=hyperlink_strainer)
    else:
        print("NOT VALID FILE: Expecting file ending in 'htm', 'html', or 'xml'")
        sys.exit()

    file_handle.close()

    print(file_tree.prettify())
