# MSWE 262P - Programming Styles
**Beautiful Soup Repository**  
Author: *Nick Hlousek*

## Repository Structure
- **Root Directory**
  - README.md
  - requirements.txt
  - **apps**
    - **m#** : Milestone # directory
        - task#.py
        - M#-README.md
  - **bs4**
    - library .py files
    - **test**
        - library test files 
         

## Environment Setup
We are going to setup a python virtual environment such that you can run any of the scripts in this project.  

1. Starting from the Root Directory of the repository create a virtual python environment

```
python3 -m venv ./StylesEnv
```

2. Activate the virtual Environment
```
source ./StylesEnv/bin/activate
```

3. Utilize the requirements.txt file to install dependencies

```
pip install -r requirements.txt
```

4. Create a symbolic link to the bs4 repository for the virtual environment
```
ln -s ../../../../bs4 ./StylesEnv/lib/python3.13/site-packages/bs4 
```

Having set up the virtual Environment in this manner as long as the bs4
directory is not moved relative to the evironment directory there will
be not issues using the local library
