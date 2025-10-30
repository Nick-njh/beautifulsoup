## Milestone-1  
by Nick Hlousek

### Directory Structure
The Directory is layed out in the following manner:
- Milestone-1
  - README.md
  - task1.py
  - task2.py
  - ...
  - task8.py 

### Dependencies
All scripts have the following two external dependencies:
1. Beautiful Soup Version 4
   - ```pip install beautifulsoup4```
2. lxml
   - ```pip install lxml```

### Running Scripts
All scripts expect the following call signature from command line and will both
complain and not run if not followed:

```python ./task#.py [HTML/XML File]```

Futhermore the Input **HTML** and **XML** files ***must*** have the following
filename extension(s):
- HTML: ```'*.html'``` or ```'*.htm'```
- XML: ```'*.xml'```

### Script Outputs
Depending on the script that script may either output to stdout or to a file.
If the script outputs to a file it will create the file in the same location as the
input file with and addtional file extenstion corresponding to the script.

For example task1.py generates a prettified version of the xml. If the input file
path was ```~/random/random/something/test.html``` then the output file would be
located and named as ```~/random/random/something/test.html.task1```.

Output List:
- task1.py: Creates file
- task2.py: Prints to stdout
- task3.py: Prints to stdout
- task4.py: Prints to stdout
- task5.py: Prints to stdout
- task6.py: Creates file
- task7.py: Creates file
- task8.py: Creates file

### Large Files
On the matter if my programs/hardware could handle opening large files here is
the data I've gathered from my tests:  

**File Size**: 1.2GB  
**Execition Time**: 32s
