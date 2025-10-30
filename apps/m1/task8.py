"""
task8.py
By Nick Hlousek

Goal of this program is to exercise some other api functionality of beautiful soup.
I've chosen to exercise deleting links and adding comments
"""

import sys
import os
from bs4 import BeautifulSoup, Comment

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("USER ERROR\nEXECUTABLE STRUCTURE: python ./task8.py [HTML/XML File]")
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

    file_handle.close()
    
    print("Thanks for Calling this program, I'll be removing any 'unnecessary links'",
          "I find and also add some helpful comments ;) just while I'm at it y'know.",
          "All for no charge btw. That's just how I roll")
    for tag in file_tree.find_all('a'):
        tag.decompose()
    for tag in file_tree.find_all(True):
        necessary_comment = Comment("HEY I THINK YOU SHOULD DELETE THIS, IT'LL MAKE IT RUN FASTER")
        tag.append(necessary_comment)
    file_tree.smooth()

    new_file = file_name + ".task8"

    if os.path.exists(new_file):
        os.remove(new_file)

    with open(new_file, "w") as storage_file:
        storage_file.write(file_tree.prettify())
    
