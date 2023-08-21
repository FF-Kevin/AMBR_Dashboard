
# AMBR DASHBOARD
## _Dashboard for AMBR Experiment Data_

#### Getting started: Installing Python
---
This tool requires the use of python, make sure to download the latest release of [Python](https://www.python.org) to make sure this works. When installing python make sure you also install pip

#### Getting Started: Installing addition packages needed
---
Before using the python script to make concat all you data make sure you install all the prereqs needed if this is your first time. Run the following command:

`pip install -r requirements.txt`

Make sure the `requirements.txt` file is from the one provided in this repository. You might have to add in the file path if it does not initially work

#### Running the Tool
---
Using a command prompt run the following command:

`python app.py`

If correctly executed, you will be prompted to enter in the file path of the AMBR data export
_Note: the file path should be to the uncompressed export file, the code will know where to navigate after_

#### Troubleshooting
---
__Issue 1: pip not found__
- If pip is not found make sure you enable the install of pip when installing python. There should be a checkbox prompting to you install pip.
- Also make sure to enable the use of PATH to allow you to run the commands on a command prompt 

__Issue 2: Error locating files__
- If issues arises where you can't fine a file try running it as a file path instead of just file name, for example:
`pip install -r "your/file/path/here/requirements.txt"`
- This might also apply when trying to run the python tool where `main.py` will need to be the file path
- You can also just change your working directory to the file where the tool is located using:
`cd your/file/path/here`