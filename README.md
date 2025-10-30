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

1. Starting from the ***Root Directory*** of the repository create a virtual python environment

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

## Running Scripts
Once the environment is setup all one needs to do to use any of the files is to make sure that
the virtual environment is active.  

This should show up in the pompt window as  

(StylesEnv) user@machine directory %

or equivalent depending on the system.  

If the environment is not showing up then make sure to activate it using the following command:
```
source ./StylesEnv/bin/activate
```
Granted this command does depending on the system that is being used but is should be relatively similar
